from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
<<<<<<< HEAD
    path('', views.home, name='home'),
    path('champions/', views.champions, name='champions'),
    # path('champions/<int:champions>/', views.champions_detail, name='detail'),
    path('champions/create/', views.ChampionCreate.as_view(), name='champions_create'),
    path('champions/<int:pk>/update/', views.ChampionUpdate.as_view(), name='champions_update'),
    path('champions/<int:pk>/delete/', views.ChampionDelete.as_view(), name='champions_delete'),
    path('augments/', views.augments, name='augments'),
    path('traits/', views.traits, name='traits_list'),
=======
    path('', views.Home.as_view(), name='home'),
    path('champions/', views.Champions.as_view(), name='champions'),
    path('champions/<int:champions>/', views._detail, name='detail'),
    path('champions/create/', views.CatCreate.as_view(), name='cats_create'),
    path('champions/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('champions/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
    path('augments/', views.Augments.as_view(), name='augments'),
    path('traits/', views.TraitsList.as_view(), name='traits_list'),
>>>>>>> 7022d29 (brian working on main branch for some reason)
]
