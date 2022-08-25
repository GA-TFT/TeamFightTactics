from django.urls import reverse
from django.db import models

# Create your models here.
class Champion(models.Model):
    ability = models.CharField(max_length=1000)
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

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'champion_id': self.id})

    class Meta:
        ordering = ['-name']

class Trait(models.Model):
    name = models.CharField(max_length=500)
    disc = models.CharField("Description", max_length=100)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'trait_id': self.id})

    class Meta:
        ordering = ['-name']