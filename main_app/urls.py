from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('champions/', views.champions, name='champions'),
    path('champions/<str:champion_name>/', views.champion_detail, name='detail'),
    path('champions/create/', views.ChampionCreate.as_view(), name='champions_create'),
    path('champions/<int:pk>/update/', views.ChampionUpdate.as_view(), name='champions_update'),
    path('champions/<int:pk>/delete/', views.ChampionDelete.as_view(), name='champions_delete'),
    path('augments/', views.augments, name='augments'),
    path('augmentgold/', views.augmentgold, name='augmentgold'),
    path('augmentprismatic/', views.augmentpris, name='augmentpris'),
    path('traits/', views.traits, name='traits'),
]
