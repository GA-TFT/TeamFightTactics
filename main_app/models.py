from django.urls import reverse
from django.db import models

# Create your models here.
class Champion(models.Model):
    ability = models.CharField(max_length=100)
    abilname = models.CharField(max_length=100)
    abilicon = models.CharField(max_length=100)
    cost = models.IntegerField()
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    armor = models.IntegerField()
    attack_speed = models.DecimalField('Attack Speed', decimal_places=2, max_digits=3)
    damage = models.IntegerField()
    hp = models.IntegerField()
    initialmama = models.IntegerField('Initial Mana')
    magic_resist = models.IntegerField('Magic Resist')
    mana = models.IntegerField()
    range = models.IntegerField()
    traits = models.CharField(max_length=100)

