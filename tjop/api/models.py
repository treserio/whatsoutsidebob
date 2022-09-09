# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Colors(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    episode = models.CharField(db_column='EPISODE', primary_key=True, max_length=30)  # Field name made lowercase.
    alizarin_crimson = models.BigIntegerField(db_column='Alizarin_Crimson', blank=True, null=True)  # Field name made lowercase.
    black_gesso = models.BigIntegerField(db_column='Black_Gesso', blank=True, null=True)  # Field name made lowercase.
    bright_red = models.BigIntegerField(db_column='Bright_Red', blank=True, null=True)  # Field name made lowercase.
    burnt_umber = models.BigIntegerField(db_column='Burnt_Umber', blank=True, null=True)  # Field name made lowercase.
    cadmium_yellow = models.BigIntegerField(db_column='Cadmium_Yellow', blank=True, null=True)  # Field name made lowercase.
    dark_sienna = models.BigIntegerField(db_column='Dark_Sienna', blank=True, null=True)  # Field name made lowercase.
    indian_red = models.BigIntegerField(db_column='Indian_Red', blank=True, null=True)  # Field name made lowercase.
    indian_yellow = models.BigIntegerField(db_column='Indian_Yellow', blank=True, null=True)  # Field name made lowercase.
    liquid_black = models.BigIntegerField(db_column='Liquid_Black', blank=True, null=True)  # Field name made lowercase.
    liquid_clear = models.BigIntegerField(db_column='Liquid_Clear', blank=True, null=True)  # Field name made lowercase.
    midnight_black = models.BigIntegerField(db_column='Midnight_Black', blank=True, null=True)  # Field name made lowercase.
    phthalo_blue = models.BigIntegerField(db_column='Phthalo_Blue', blank=True, null=True)  # Field name made lowercase.
    phthalo_green = models.BigIntegerField(db_column='Phthalo_Green', blank=True, null=True)  # Field name made lowercase.
    prussian_blue = models.BigIntegerField(db_column='Prussian_Blue', blank=True, null=True)  # Field name made lowercase.
    sap_green = models.BigIntegerField(db_column='Sap_Green', blank=True, null=True)  # Field name made lowercase.
    titanium_white = models.BigIntegerField(db_column='Titanium_White', blank=True, null=True)  # Field name made lowercase.
    van_dyke_brown = models.BigIntegerField(db_column='Van_Dyke_Brown', blank=True, null=True)  # Field name made lowercase.
    yellow_ochre = models.BigIntegerField(db_column='Yellow_Ochre', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = False
        db_table = 'colors'


class HexValues(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    color = models.TextField(blank=True, null=False, primary_key=True,)
    hex = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hex_values'


class PicInfo(models.Model):
    index = models.BigIntegerField(blank=True, primary_key=True, null=False)
    episode_colors = models.ForeignKey('Colors', models.DO_NOTHING, db_column='episode_colors', blank=True, null=True)  # Field name made lowercase.
    episode_subjects = models.ForeignKey('Subjects', models.DO_NOTHING, db_column='episode_subjects', blank=True, null=True)  # Field name made lowercase.
    # episode = models.CharField(db_column='EPISODE', primary_key=True, max_length=30)  # Field name made lowercase.
    painting_index = models.BigIntegerField(blank=True, null=True)
    img_src = models.TextField(blank=True, null=True)
    painting_title = models.TextField(blank=True, null=True)
    season = models.BigIntegerField(blank=True, null=True)
    episode_num = models.BigIntegerField(blank=True, null=True)
    num_colors = models.BigIntegerField(blank=True, null=True)
    youtube_src = models.TextField(blank=True, null=True)
    air_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pic_info'


class Subjects(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    episode = models.CharField(db_column='EPISODE', primary_key=True, max_length=30)  # Field name made lowercase.
    apple_frame = models.BigIntegerField(db_column='APPLE_FRAME', blank=True, null=True)  # Field name made lowercase.
    aurora_borealis = models.BigIntegerField(db_column='AURORA_BOREALIS', blank=True, null=True)  # Field name made lowercase.
    barn = models.BigIntegerField(db_column='BARN', blank=True, null=True)  # Field name made lowercase.
    beach = models.BigIntegerField(db_column='BEACH', blank=True, null=True)  # Field name made lowercase.
    boat = models.BigIntegerField(db_column='BOAT', blank=True, null=True)  # Field name made lowercase.
    bridge = models.BigIntegerField(db_column='BRIDGE', blank=True, null=True)  # Field name made lowercase.
    building = models.BigIntegerField(db_column='BUILDING', blank=True, null=True)  # Field name made lowercase.
    bushes = models.BigIntegerField(db_column='BUSHES', blank=True, null=True)  # Field name made lowercase.
    cabin = models.BigIntegerField(db_column='CABIN', blank=True, null=True)  # Field name made lowercase.
    cactus = models.BigIntegerField(db_column='CACTUS', blank=True, null=True)  # Field name made lowercase.
    circle_frame = models.BigIntegerField(db_column='CIRCLE_FRAME', blank=True, null=True)  # Field name made lowercase.
    cirrus = models.BigIntegerField(db_column='CIRRUS', blank=True, null=True)  # Field name made lowercase.
    cliff = models.BigIntegerField(db_column='CLIFF', blank=True, null=True)  # Field name made lowercase.
    clouds = models.BigIntegerField(db_column='CLOUDS', blank=True, null=True)  # Field name made lowercase.
    conifer = models.BigIntegerField(db_column='CONIFER', blank=True, null=True)  # Field name made lowercase.
    cumulus = models.BigIntegerField(db_column='CUMULUS', blank=True, null=True)  # Field name made lowercase.
    deciduous = models.BigIntegerField(db_column='DECIDUOUS', blank=True, null=True)  # Field name made lowercase.
    diane_andre = models.BigIntegerField(db_column='DIANE_ANDRE', blank=True, null=True)  # Field name made lowercase.
    dock = models.BigIntegerField(db_column='DOCK', blank=True, null=True)  # Field name made lowercase.
    double_oval_frame = models.BigIntegerField(db_column='DOUBLE_OVAL_FRAME', blank=True, null=True)  # Field name made lowercase.
    farm = models.BigIntegerField(db_column='FARM', blank=True, null=True)  # Field name made lowercase.
    fence = models.BigIntegerField(db_column='FENCE', blank=True, null=True)  # Field name made lowercase.
    fire = models.BigIntegerField(db_column='FIRE', blank=True, null=True)  # Field name made lowercase.
    florida_frame = models.BigIntegerField(db_column='FLORIDA_FRAME', blank=True, null=True)  # Field name made lowercase.
    flowers = models.BigIntegerField(db_column='FLOWERS', blank=True, null=True)  # Field name made lowercase.
    fog = models.BigIntegerField(db_column='FOG', blank=True, null=True)  # Field name made lowercase.
    framed = models.BigIntegerField(db_column='FRAMED', blank=True, null=True)  # Field name made lowercase.
    grass = models.BigIntegerField(db_column='GRASS', blank=True, null=True)  # Field name made lowercase.
    guest = models.BigIntegerField(db_column='GUEST', blank=True, null=True)  # Field name made lowercase.
    half_circle_frame = models.BigIntegerField(db_column='HALF_CIRCLE_FRAME', blank=True, null=True)  # Field name made lowercase.
    half_oval_frame = models.BigIntegerField(db_column='HALF_OVAL_FRAME', blank=True, null=True)  # Field name made lowercase.
    hills = models.BigIntegerField(db_column='HILLS', blank=True, null=True)  # Field name made lowercase.
    lake = models.BigIntegerField(db_column='LAKE', blank=True, null=True)  # Field name made lowercase.
    lakes = models.BigIntegerField(db_column='LAKES', blank=True, null=True)  # Field name made lowercase.
    lighthouse = models.BigIntegerField(db_column='LIGHTHOUSE', blank=True, null=True)  # Field name made lowercase.
    mill = models.BigIntegerField(db_column='MILL', blank=True, null=True)  # Field name made lowercase.
    moon = models.BigIntegerField(db_column='MOON', blank=True, null=True)  # Field name made lowercase.
    mountain = models.BigIntegerField(db_column='MOUNTAIN', blank=True, null=True)  # Field name made lowercase.
    mountains = models.BigIntegerField(db_column='MOUNTAINS', blank=True, null=True)  # Field name made lowercase.
    night = models.BigIntegerField(db_column='NIGHT', blank=True, null=True)  # Field name made lowercase.
    ocean = models.BigIntegerField(db_column='OCEAN', blank=True, null=True)  # Field name made lowercase.
    oval_frame = models.BigIntegerField(db_column='OVAL_FRAME', blank=True, null=True)  # Field name made lowercase.
    palm_trees = models.BigIntegerField(db_column='PALM_TREES', blank=True, null=True)  # Field name made lowercase.
    path = models.BigIntegerField(db_column='PATH', blank=True, null=True)  # Field name made lowercase.
    person = models.BigIntegerField(db_column='PERSON', blank=True, null=True)  # Field name made lowercase.
    portrait = models.BigIntegerField(db_column='PORTRAIT', blank=True, null=True)  # Field name made lowercase.
    rectangle_3d_frame = models.BigIntegerField(db_column='RECTANGLE_3D_FRAME', blank=True, null=True)  # Field name made lowercase.
    rectangular_frame = models.BigIntegerField(db_column='RECTANGULAR_FRAME', blank=True, null=True)  # Field name made lowercase.
    river = models.BigIntegerField(db_column='RIVER', blank=True, null=True)  # Field name made lowercase.
    rocks = models.BigIntegerField(db_column='ROCKS', blank=True, null=True)  # Field name made lowercase.
    seashell_frame = models.BigIntegerField(db_column='SEASHELL_FRAME', blank=True, null=True)  # Field name made lowercase.
    snow = models.BigIntegerField(db_column='SNOW', blank=True, null=True)  # Field name made lowercase.
    snowy_mountain = models.BigIntegerField(db_column='SNOWY_MOUNTAIN', blank=True, null=True)  # Field name made lowercase.
    split_frame = models.BigIntegerField(db_column='SPLIT_FRAME', blank=True, null=True)  # Field name made lowercase.
    steve_ross = models.BigIntegerField(db_column='STEVE_ROSS', blank=True, null=True)  # Field name made lowercase.
    structure = models.BigIntegerField(db_column='STRUCTURE', blank=True, null=True)  # Field name made lowercase.
    sun = models.BigIntegerField(db_column='SUN', blank=True, null=True)  # Field name made lowercase.
    tomb_frame = models.BigIntegerField(db_column='TOMB_FRAME', blank=True, null=True)  # Field name made lowercase.
    tree = models.BigIntegerField(db_column='TREE', blank=True, null=True)  # Field name made lowercase.
    trees = models.BigIntegerField(db_column='TREES', blank=True, null=True)  # Field name made lowercase.
    triple_frame = models.BigIntegerField(db_column='TRIPLE_FRAME', blank=True, null=True)  # Field name made lowercase.
    waterfall = models.BigIntegerField(db_column='WATERFALL', blank=True, null=True)  # Field name made lowercase.
    waves = models.BigIntegerField(db_column='WAVES', blank=True, null=True)  # Field name made lowercase.
    windmill = models.BigIntegerField(db_column='WINDMILL', blank=True, null=True)  # Field name made lowercase.
    window_frame = models.BigIntegerField(db_column='WINDOW_FRAME', blank=True, null=True)  # Field name made lowercase.
    winter = models.BigIntegerField(db_column='WINTER', blank=True, null=True)  # Field name made lowercase.
    wood_framed = models.BigIntegerField(db_column='WOOD_FRAMED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subjects'


