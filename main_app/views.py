from hmac import compare_digest
from django.shortcuts import render
from .models import Augment, Champion, Trait, Video, Comp
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(request):
  videos = Video.objects.all()
  comps = Comp.objects.all()
  context = {
    'videos': videos, 
    'comps': comps
    }
  
  return render(request, 'home.html', context)

def champions(request):
  champions = Champion.objects.all()
  return render(request, 'champions.html', {'champions': champions})

def champion_detail(request, champion_name):
  champion = Champion.objects.get(name=champion_name)
  traits = Trait.objects.all()
  return render(request, 'championdetail.html', {'champion': champion, 'traits':traits})

def traits(request):
  traits = Trait.objects.all()
  return render(request, 'traits.html', {'traits': traits})

def augments(request):
  augmentSilver = Augment.objects.filter(tier=1)
  return render(request, 'augments.html', {'augments': augmentSilver})

def augmentgold(request):
  augmentGold = Augment.objects.filter(tier=2)
  return render(request, 'augmentgold.html', {'augments': augmentGold})
  
def augmentpris(request):
  augmentPris = Augment.objects.filter(tier=3)
  return render(request, 'augmentpris.html', {'augments': augmentPris})
