from django.shortcuts import render
from .models import Augment, Champion, Trait, Video, TraitImage
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(request):
  videos = Video.objects.all()
  return render(request, 'home.html', {'videos': videos})

def champions(request):
  champions = Champion.objects.all()
  return render(request, 'champions.html', {'champions': champions})

def champion_detail(request, champion_name):
  champion = Champion.objects.get(name=champion_name)
  traits = Trait.objects.all()
  return render(request, 'championdetail.html', {'champion': champion, 'traits':traits})

def traits(request):
  traits = Trait.objects.all()
  return render(request, 'traits.html', {'traits': traits, 'traitimg':traitimg})

def augments(request):
  augmentSilver = Augment.objects.filter(tier=1)
  return render(request, 'augments.html', {'augments': augmentSilver})

def augmentgold(request):
  augmentGold = Augment.objects.filter(tier=2)
  return render(request, 'augmentgold.html', {'augments': augmentGold})
  
def augmentpris(request):
  augmentPris = Augment.objects.filter(tier=3)
  return render(request, 'augmentpris.html', {'augments': augmentPris})

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


class TraitCreate(CreateView):
  model = Trait
  fields = '__all__'

class TraitUpdate(UpdateView):
  model = Trait
  fields = ['name', 'disc', 'icon']

class TraitDelete(DeleteView):
  model = Trait
  success_url = '/traits/'

class AugmentCreate(CreateView):
  model = Augment
  fields = '__all__'

class AugmentUpdate(UpdateView):
  model = Augment
  fields = ['name', 'teir', 'desc', 'icon']

class AugmentDelete(DeleteView):
  model = Augment
  success_url = '/augments/'

class VideoCreate(CreateView):
  model = Video
  fields = '__all__'

class VideoUpdate(UpdateView):
  model = Video
  fields = ['title', 'url']

class VideoDelete(DeleteView):
  model = Video
  success_url = '/videos/'

class TraitImageCreate(CreateView):
  model = TraitImage
  fields = '__all__'

class TraitImageUpdate(UpdateView):
  model = TraitImage
  fields = ['name', 'image', 'charimg']

class TraitImageDelete(DeleteView):
  model = TraitImage
  success_url = '/traitimg/'