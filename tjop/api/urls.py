from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api'

urlpatterns = [
    path('hex_values/', views.hex_values.as_view()),
    path('pic_info/', views.pic_info.as_view()),
    path('colors/', views.colors.as_view()),
    path('subjects/', views.subj_view.as_view()),
    path('all_info/', views.join_table.as_view())
]
