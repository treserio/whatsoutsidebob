from rest_framework import serializers
from . import models
from django.contrib.auth import authenticate
from .models import HexValues


class ColorsSeri(serializers.ModelSerializer):
    class Meta:
        model = models.Colors
        fields = [
            'episode',
            'alizarin_crimson',
            'black_gesso',
            'bright_red',
            'burnt_umber',
            'cadmium_yellow',
            'dark_sienna',
            'indian_red',
            'indian_yellow',
            'liquid_black',
            'liquid_clear',
            'midnight_black',
            'phthalo_blue',
            'phthalo_green',
            'prussian_blue',
            'sap_green',
            'titanium_white',
            'van_dyke_brown',
            'yellow_ochre',
        ]

class HexValuesSeri(serializers.ModelSerializer):
    class Meta:
        model = models.HexValues
        fields = [
            'index',
            'color',
            'hex'
        ]

class JoinTableSeri(serializers.ModelSerializer):
    class Meta:
        model = models.PicInfo
        fields = [
            'index',
            'episode',
            'painting_index',
            'img_src',
            'painting_title',
            'season',
            'episode_num',
            'num_colors',
            'youtube_src',
            'air_date',
            'colors_used',
            'subjects',
        ]

    episode = serializers.SerializerMethodField(read_only=True)
    def get_episode(self, obj):
        return obj.episode_colors.episode

    colors_used = serializers.SerializerMethodField(read_only=True)
    def get_colors_used(self, obj):
        color_list = [
            'alizarin_crimson',
            'black_gesso',
            'bright_red',
            'burnt_umber',
            'cadmium_yellow',
            'dark_sienna',
            'indian_red',
            'indian_yellow',
            'liquid_black',
            'liquid_clear',
            'midnight_black',
            'phthalo_blue',
            'phthalo_green',
            'prussian_blue',
            'sap_green',
            'titanium_white',
            'van_dyke_brown',
            'yellow_ochre',
        ]
        # used to create colors_used index for output
        hexes = HexValues.objects.all().order_by('color')
        ###
        #   create the colors_used value and store in each queried item
        ###
        color_hexes = {}
        for i in range(len(color_list)):
            if getattr(obj.episode_colors, color_list[i]) == 1:
                color_hexes.update({' '.join(color_list[i].split('_')).title():
                hexes.filter(color=' '.join(color_list[i].split('_')).title())[0].hex
            })
        return color_hexes

    subjects = serializers.SerializerMethodField(read_only=True)
    def get_subjects(self, obj):
        subj_list = [
            'episode',
            'apple_frame',
            'aurora_borealis',
            'barn',
            'beach',
            'boat',
            'bridge',
            'building',
            'bushes',
            'cabin',
            'cactus',
            'circle_frame',
            'cirrus',
            'cliff',
            'clouds',
            'conifer',
            'cumulus',
            'deciduous',
            'diane_andre',
            'dock',
            'double_oval_frame',
            'farm',
            'fence',
            'fire',
            'florida_frame',
            'flowers',
            'fog',
            'framed',
            'grass',
            'guest',
            'half_circle_frame',
            'half_oval_frame',
            'hills',
            'lake',
            'lakes',
            'lighthouse',
            'mill',
            'moon',
            'mountain',
            'mountains',
            'night',
            'ocean',
            'oval_frame',
            'palm_trees',
            'path',
            'person',
            'portrait',
            'rectangle_3d_frame',
            'rectangular_frame',
            'river',
            'rocks',
            'seashell_frame',
            'snow',
            'snowy_mountain',
            'split_frame',
            'steve_ross',
            'structure',
            'sun',
            'tomb_frame',
            'tree',
            'trees',
            'triple_frame',
            'waterfall',
            'waves',
            'windmill',
            'window_frame',
            'winter',
            'wood_framed',
        ]
        return [subj for subj in subj_list if getattr(obj.episode_subjects, subj) == 1]


class PicInfoSeri(serializers.ModelSerializer):
    episode = serializers.SerializerMethodField(read_only=True)
    def get_episode(self, obj):
        return obj.episode_colors.episode
    class Meta:
        model = models.PicInfo
        fields = [
            'index',
            'episode',
            'painting_index',
            'img_src',
            'painting_title',
            'season',
            'episode_num',
            'num_colors',
            'youtube_src',
            'air_date'
        ]

class SubjectsSeri(serializers.ModelSerializer):
    class Meta:
        model = models.Subjects
        fields = [
            'episode',
            'apple_frame',
            'aurora_borealis',
            'barn',
            'beach',
            'boat',
            'bridge',
            'building',
            'bushes',
            'cabin',
            'cactus',
            'circle_frame',
            'cirrus',
            'cliff',
            'clouds',
            'conifer',
            'cumulus',
            'deciduous',
            'diane_andre',
            'dock',
            'double_oval_frame',
            'farm',
            'fence',
            'fire',
            'florida_frame',
            'flowers',
            'fog',
            'framed',
            'grass',
            'guest',
            'half_circle_frame',
            'half_oval_frame',
            'hills',
            'lake',
            'lakes',
            'lighthouse',
            'mill',
            'moon',
            'mountain',
            'mountains',
            'night',
            'ocean',
            'oval_frame',
            'palm_trees',
            'path',
            'person',
            'portrait',
            'rectangle_3d_frame',
            'rectangular_frame',
            'river',
            'rocks',
            'seashell_frame',
            'snow',
            'snowy_mountain',
            'split_frame',
            'steve_ross',
            'structure',
            'sun',
            'tomb_frame',
            'tree',
            'trees',
            'triple_frame',
            'waterfall',
            'waves',
            'windmill',
            'window_frame',
            'winter',
            'wood_framed',
        ]
