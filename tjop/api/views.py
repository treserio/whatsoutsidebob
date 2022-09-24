# from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, views
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt
import json



from .models import Colors, HexValues, PicInfo, Subjects
from .serializers import ColorsSeri, HexValuesSeri, JoinTableSeri, PicInfoSeri, SubjectsSeri


class colors(ListAPIView):
    ordering = ['episode']
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Colors.objects.all()
    serializer_class = ColorsSeri
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = [
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
    ordering_fields = [
        'episode'
    ]
    search_fields = [
        'episode'
    ]

class hex_values(ListAPIView):
    ordering = ['index']
    permission_classes = (permissions.IsAuthenticated,)
    queryset = HexValues.objects.all()
    serializer_class = HexValuesSeri
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = [
        'index',
        'color',
        'hex'
    ]
    ordering_fields = [
        'index',
        'color',
    ]
    search_fields = [
        'color',
    ]

class join_table(ListAPIView):
    ordering = ['episode_colors__episode']
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = PicInfo.objects.all()
    serializer_class = JoinTableSeri
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = {
        # PIC_INFO
        'episode_colors__episode': ['exact', 'icontains'],
        'painting_index': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'painting_title': ['exact', 'icontains'],
        'season': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'episode_num': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'num_colors': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'air_date': ['lt', 'gt', 'lte', 'gte', 'exact'],
        # COLORS
        'episode_colors__alizarin_crimson': ['exact'],
        'episode_colors__black_gesso': ['exact'],
        'episode_colors__bright_red': ['exact'],
        'episode_colors__burnt_umber': ['exact'],
        'episode_colors__cadmium_yellow': ['exact'],
        'episode_colors__dark_sienna': ['exact'],
        'episode_colors__indian_red': ['exact'],
        'episode_colors__indian_yellow': ['exact'],
        'episode_colors__liquid_black': ['exact'],
        'episode_colors__liquid_clear': ['exact'],
        'episode_colors__midnight_black': ['exact'],
        'episode_colors__phthalo_blue': ['exact'],
        'episode_colors__phthalo_green': ['exact'],
        'episode_colors__prussian_blue': ['exact'],
        'episode_colors__sap_green': ['exact'],
        'episode_colors__titanium_white': ['exact'],
        'episode_colors__van_dyke_brown': ['exact'],
        'episode_colors__yellow_ochre': ['exact'],
        # SUBJECTS
        'episode_subjects__apple_frame': ['exact'],
        'episode_subjects__aurora_borealis': ['exact'],
        'episode_subjects__barn': ['exact'],
        'episode_subjects__beach': ['exact'],
        'episode_subjects__boat': ['exact'],
        'episode_subjects__bridge': ['exact'],
        'episode_subjects__building': ['exact'],
        'episode_subjects__bushes': ['exact'],
        'episode_subjects__cabin': ['exact'],
        'episode_subjects__cactus': ['exact'],
        'episode_subjects__circle_frame': ['exact'],
        'episode_subjects__cirrus': ['exact'],
        'episode_subjects__cliff': ['exact'],
        'episode_subjects__clouds': ['exact'],
        'episode_subjects__conifer': ['exact'],
        'episode_subjects__cumulus': ['exact'],
        'episode_subjects__deciduous': ['exact'],
        'episode_subjects__diane_andre': ['exact'],
        'episode_subjects__dock': ['exact'],
        'episode_subjects__double_oval_frame': ['exact'],
        'episode_subjects__farm': ['exact'],
        'episode_subjects__fence': ['exact'],
        'episode_subjects__fire': ['exact'],
        'episode_subjects__florida_frame': ['exact'],
        'episode_subjects__flowers': ['exact'],
        'episode_subjects__fog': ['exact'],
        'episode_subjects__framed': ['exact'],
        'episode_subjects__grass': ['exact'],
        'episode_subjects__guest': ['exact'],
        'episode_subjects__half_circle_frame': ['exact'],
        'episode_subjects__half_oval_frame': ['exact'],
        'episode_subjects__hills': ['exact'],
        'episode_subjects__lake': ['exact'],
        'episode_subjects__lakes': ['exact'],
        'episode_subjects__lighthouse': ['exact'],
        'episode_subjects__mill': ['exact'],
        'episode_subjects__moon': ['exact'],
        'episode_subjects__mountain': ['exact'],
        'episode_subjects__mountains': ['exact'],
        'episode_subjects__night': ['exact'],
        'episode_subjects__ocean': ['exact'],
        'episode_subjects__oval_frame': ['exact'],
        'episode_subjects__palm_trees': ['exact'],
        'episode_subjects__path': ['exact'],
        'episode_subjects__person': ['exact'],
        'episode_subjects__portrait': ['exact'],
        'episode_subjects__rectangle_3d_frame': ['exact'],
        'episode_subjects__rectangular_frame': ['exact'],
        'episode_subjects__river': ['exact'],
        'episode_subjects__rocks': ['exact'],
        'episode_subjects__seashell_frame': ['exact'],
        'episode_subjects__snow': ['exact'],
        'episode_subjects__snowy_mountain': ['exact'],
        'episode_subjects__split_frame': ['exact'],
        'episode_subjects__steve_ross': ['exact'],
        'episode_subjects__structure': ['exact'],
        'episode_subjects__sun': ['exact'],
        'episode_subjects__tomb_frame': ['exact'],
        'episode_subjects__tree': ['exact'],
        'episode_subjects__trees': ['exact'],
        'episode_subjects__triple_frame': ['exact'],
        'episode_subjects__waterfall': ['exact'],
        'episode_subjects__waves': ['exact'],
        'episode_subjects__windmill': ['exact'],
        'episode_subjects__window_frame': ['exact'],
        'episode_subjects__winter': ['exact'],
        'episode_subjects__wood_framed': ['exact'],
    }
    search_fields = [
        'episode_colors__episode',
        'painting_index',
        'painting_title',
        'season',
        'episode_num',
        'num_colors',
        'air_date'
    ]
    ordering_fields = [
        'episode_colors__episode',
        'painting_index',
        'painting_title',
        'season',
        'episode_num',
        'num_colors',
        'air_date'
    ]

class pic_info(ListAPIView):
    ordering = ['episode_colors__episode']
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = PicInfo.objects.all()
    serializer_class = PicInfoSeri
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = {
        'episode_colors__episode': ['exact', 'icontains'],
        'painting_index': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'painting_title': ['exact', 'icontains'],
        'season': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'episode_num': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'num_colors': ['lt', 'gt', 'lte', 'gte', 'exact'],
        'air_date': ['lt', 'gt', 'lte', 'gte', 'exact'],
    }
    ordering_fields = [
        'episode_colors',
        'painting_index',
        'painting_title',
        'season',
        'episode_num',
        'num_colors',
        'air_date'
    ]
    search_fields = [
        'episode_colors__episode',
        'painting_index',
        'painting_title',
        'season',
        'episode_num',
        'num_colors',
        'air_date'
    ]

class subj_view(ListAPIView):
    ordering = ['episode']
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSeri
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = {
        'episode': ['exact', 'icontains'],
        'apple_frame': ['exact'],
        'aurora_borealis': ['exact'],
        'barn': ['exact'],
        'beach': ['exact'],
        'boat': ['exact'],
        'bridge': ['exact'],
        'building': ['exact'],
        'bushes': ['exact'],
        'cabin': ['exact'],
        'cactus': ['exact'],
        'circle_frame': ['exact'],
        'cirrus': ['exact'],
        'cliff': ['exact'],
        'clouds': ['exact'],
        'conifer': ['exact'],
        'cumulus': ['exact'],
        'deciduous': ['exact'],
        'diane_andre': ['exact'],
        'dock': ['exact'],
        'double_oval_frame': ['exact'],
        'farm': ['exact'],
        'fence': ['exact'],
        'fire': ['exact'],
        'florida_frame': ['exact'],
        'flowers': ['exact'],
        'fog': ['exact'],
        'framed': ['exact'],
        'grass': ['exact'],
        'guest': ['exact'],
        'half_circle_frame': ['exact'],
        'half_oval_frame': ['exact'],
        'hills': ['exact'],
        'lake': ['exact'],
        'lakes': ['exact'],
        'lighthouse': ['exact'],
        'mill': ['exact'],
        'moon': ['exact'],
        'mountain': ['exact'],
        'mountains': ['exact'],
        'night': ['exact'],
        'ocean': ['exact'],
        'oval_frame': ['exact'],
        'palm_trees': ['exact'],
        'path': ['exact'],
        'person': ['exact'],
        'portrait': ['exact'],
        'rectangle_3d_frame': ['exact'],
        'rectangular_frame': ['exact'],
        'river': ['exact'],
        'rocks': ['exact'],
        'seashell_frame': ['exact'],
        'snow': ['exact'],
        'snowy_mountain': ['exact'],
        'split_frame': ['exact'],
        'steve_ross': ['exact'],
        'structure': ['exact'],
        'sun': ['exact'],
        'tomb_frame': ['exact'],
        'tree': ['exact'],
        'trees': ['exact'],
        'triple_frame': ['exact'],
        'waterfall': ['exact'],
        'waves': ['exact'],
        'windmill': ['exact'],
        'window_frame': ['exact'],
        'winter': ['exact'],
        'wood_framed': ['exact'],
    }
    ordering_fields = [
        'episode'
    ]
    search_fields = [
        'episode'
    ]

class logout(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, req):
        return self.logout(req)

    def logout(self, req):
        try:
            Token.objects.get(**{'key':req.META['HTTP_AUTHORIZATION'].split(' ')[1]}).delete()
            return HttpResponse('Token has been removed')
        except Exception:
            return HttpResponse("Invalid Token, please try again")

@csrf_exempt
def register(request):
    from django.contrib.auth.models import User

    if request.method == 'POST':
        input = json.loads(request.body.decode('utf-8'))
        try:
            user = User.objects.create_user(
            username=input['username'],
            first_name=input['firstname'],
            last_name=input['lastname'],
            email=input['email'],
            password=input['password'],
        )
            return HttpResponse('User has been created')
        except Exception as e:
            print('👁👅👁')
            print(e)
            return HttpResponse('User already exists', status=409)
