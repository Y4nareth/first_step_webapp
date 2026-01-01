from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gm_view/', views.gm_dashboard, name='gm_view'),
    path('player_view/', views.player_view, name='player_view'),
]