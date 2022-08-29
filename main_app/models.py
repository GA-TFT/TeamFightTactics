from django.urls import reverse
from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class Comp(models.Model):
    name = models.CharField(max_length=500)
    tier = models.CharField(max_length=500)
    desc = models.CharField(max_length=500)
    imgone = models.CharField(max_length=500)
    imgtwo = models.CharField(max_length=500)
    imgthree = models.CharField(max_length=500)
    imgfour =models.CharField(max_length=500)
    imgfive = models.CharField(max_length=500)
    imgsix = models.CharField(max_length=500)
    imgseven = models.CharField(max_length=500)
    nameone = models.CharField(max_length=500)
    nametwo = models.CharField(max_length=500)
    namethree = models.CharField(max_length=500)
    namefour =models.CharField(max_length=500)
    namefive = models.CharField(max_length=500)
    namesix = models.CharField(max_length=500)
    nameseven = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
class Trait(models.Model):
    name = models.CharField(max_length=500)
    desc = models.CharField("Description", max_length=900)
    icon = models.CharField(max_length=100)
    champions = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'trait_id': self.id})

    class Meta:
        ordering = ['name']

class Traitimg(models.Model):
    charname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='main_app/static/images/home', blank=True)
    charimage = models.ForeignKey(Trait, related_name='traitimage', on_delete=models.CASCADE)


class Champion(models.Model):
    ability = models.CharField(max_length=500)
    abilname = models.CharField(max_length=100)
    abilicon = models.CharField(max_length=100)
    cost = models.IntegerField()
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    armor = models.IntegerField()
    attack_speed = models.DecimalField('Attack Speed', decimal_places=2, max_digits=3)
    damage = models.CharField("Damage", max_length=100)
    hp = models.CharField("Health", max_length=100)
    initialmana = models.CharField('Mana', max_length=100)
    magic_resist = models.IntegerField('Magic Resist')
    range = models.IntegerField()
    trait = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_url(self):
        return reverse('detail', kwargs={'champion_name': self.name})

    class Meta:
        ordering = ['name']

class Augment(models.Model):
    name = models.CharField(max_length=500)
    tier = models.IntegerField()
    desc = models.CharField("Description", max_length=900)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'augment_id': self.id})
    

    class Meta:
        ordering = ['name']

class Video(models.Model):
    title = models.CharField(max_length=100)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)

