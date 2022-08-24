from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
<<<<<<< HEAD
<<<<<<< HEAD
from .models import Champion
from django.views.generic.edit import CreateView, UpdateView, DeleteView
=======
=======
from .models import Champion
from django.views.generic.edit import CreateView, UpdateView, DeleteView

>>>>>>> 188ec36 (CRUD)
import json
>>>>>>> f79beff (rebase)

import json

def home(request):
  return render(request, 'home.html')

def champions(request):
  return render(request, 'champions.html')

def augments(request):
  return render(request, 'augments.html')

def traits(request):
  return render(request, 'traits.html')

# def champions_index(request):
#   champions = Champion.objects.all()
#   return render(request, 'champions/index.html', {'champions': champions})

# def champions_detail(request, champion_id):
#   champion = Champion.objects.get(id=champion_id)
#   return render(request, 'champions/detail.html')

# Class-Based View (CBV)
class ChampionCreate(CreateView):
  model = Champion
  fields = '__all__'

class ChampionUpdate(UpdateView):
  model = Champion
  fields = ['ability', 'abilname', 'abilicon', 'cost', 'name', 'icon', 'armor', 'attack_speed', 'damage', 'hp', 'initialmana', 'magic_resist', 'mana', 'range', 'traits']

class ChampionDelete(DeleteView):
  model = Champion
  success_url = '/champions/'

<<<<<<< HEAD
=======
# champion = [
#     Champions("Aatrox", "https://cdn.mobalytics.gg/assets/tft/images/champions/page-background/set7/aatrox.jpg", "Shimmerscale, Warrior", "1"),
# ]

# Class-Based View (CBV)
class ChampionCreate(CreateView):
  model = Champion
  fields = '__all__'

class ChampionUpdate(UpdateView):
  model = Champion
  fields = ['ability', 'abilname', 'abilicon', 'cost', 'name', 'icon', 'armor', 'attack_speed', 'damage', 'hp', 'initialmana', 'magic_resist', 'mana', 'range', 'traits']

class ChampionDelete(DeleteView):
  model = Champion
  success_url = '/champions/'

>>>>>>> 188ec36 (CRUD)
