import pandas as pd
import re
from datetime import datetime
from sqlalchemy import create_engine

# Prep for running load.py
# bob_ross database must be setup first
# index needs to be added as the column name to the first field in 'TJOP - Colors Used'
engine = create_engine('mysql://root:root@localhost:3306/bob_ross')

colors_used = pd.read_csv('./TJOP - Colors Used')
subject_matter = pd.read_csv('./TJOP - Subject Matter')
sub_matter2 = pd.read_csv('./TJOP - Subject Matter')
sub_matter3 = pd.read_csv('./TJOP - Subject Matter')

# print(colors_used)
# print(type(colors_used))
# print(colors_used.__dict__)
# print('\n'.join(f'{col}' for col in colors_used.columns))

###
#   get our list of episode strings to use for joins in most tables, and set to a pandas dataframe
###
episode_DF = subject_matter['EPISODE']
epi_subjs = sub_matter2['EPISODE']
epi_colors = sub_matter3['EPISODE']
epi_subjs.name = 'episode_subjects'
epi_colors.name = 'episode_colors'
print(epi_subjs, '\n\n', epi_colors)
print(epi_colors.name, epi_subjs.name, episode_DF.name)

###
#   create subjects table without the TITLE field
###
subject_matter.drop(['TITLE'], axis=1, inplace=True)
subject_matter.to_sql('subjects', con=engine, if_exists='replace')

###
#   create the pic_info table by filtering and adding various column data with pandas dataframes
###
episodeDates = [re.findall(r'[\w\s]\(([\d\w,\s]+)\)[$ ]?', line)[0]
                for line in open('TJOP - Episode Dates')]
date_objects = [datetime.strptime(date, '%B %d, %Y') for date in episodeDates]
# print(date_objects)
date_DF = pd.DataFrame()
date_DF['air_date'] = date_objects

main_drop_list = [
    'index',
    'Black_Gesso',
    'Bright_Red',
    'Burnt_Umber',
    'Cadmium_Yellow',
    'Dark_Sienna',
    'Indian_Red',
    'Indian_Yellow',
    'Liquid_Black',
    'Liquid_Clear',
    'Midnight_Black',
    'Phthalo_Blue',
    'Phthalo_Green',
    'Prussian_Blue',
    'Sap_Green',
    'Titanium_White',
    'Van_Dyke_Brown',
    'Yellow_Ochre',
    'Alizarin_Crimson',
    'colors',
    'color_hex',
]

# create a clean dataframe to use for our main import
main_DF = colors_used.drop(main_drop_list, axis=1)
# rename the episode column to allow the use of the EPISODE column
main_DF.columns = main_DF.columns.str.replace('episode', 'episode_num')
# concatonate all data frames into a single import source
main_import = pd.concat([epi_colors, epi_subjs, main_DF, date_DF], axis=1)
# print(main_import.columns)
# create our table using to_sql
main_import.to_sql('pic_info', con=engine, if_exists='replace')

###
#   Create the colors table from the dataframes
###
colors_drop_list = ['index', 'painting_index', 'img_src', 'painting_title',
                    'season', 'episode', 'num_colors', 'youtube_src', 'colors', 'color_hex']
# concate the episode_DF with the dataframe of dropped columns from colors_used
colors_import = pd.concat(
    [episode_DF, colors_used.drop(colors_drop_list, axis=1)], axis=1)
# print(colors_import.columns)
# create our table using to_sql
colors_import.to_sql('colors', con=engine, if_exists='replace')

###
#   create list of hex values for colors_hex table
###
hex_DF = colors_used[['colors', 'color_hex']]
# print(hex_DF)
# setup key value pairs based on string input from rows of hex_DF, all col values of hex_DF start as strings
hex_colors = {}
for k, v in hex_DF.iterrows():
    color_list = v.colors[1:-1].replace("'", '').replace(
        '\\r', '').replace('\\n', '').split(', ')
    hex_list = v.color_hex[1:-1].replace("'", '').replace(
        '\\r', '').replace('\\n', '').split(', ')
    hex_colors.update({color_list[i]: hex_list[i]
                      for i in range(len(color_list))})
hex_import = pd.DataFrame(
    {'color': hex_colors.keys(), 'hex': hex_colors.values()})
hex_import.to_sql('hex_values', con=engine, if_exists='replace')

###
#   working with sqlAlchemy cursor example, get the list of colors from the colors table
###
# conn = engine.connect()
# sql_exec = 'SELECT * FROM colors WHERE EPISODE = "S01E01"'
# ret_val = conn.execute(sql_exec).mappings().all()[0]
# print(ret_val)
# return_colors = [ k for k, v in ret_val.items() if v == 1 ]
# print('\nreturn_colors\n', return_colors)
# # close our sql connection
# conn.close()
