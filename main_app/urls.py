from django.urls import path 
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('champions/', views.Champions.as_view(), name='champions'),
    path('augments/', views.Augments.as_view(), name='augments'),
    path('traits/', views.TraitsList.as_view(), name='traits_list'),
]