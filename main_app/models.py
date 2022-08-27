from django.urls import reverse
from django.db import models

# Create your models here.
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
    traits = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'champion_id': self.id})

    class Meta:
        ordering = ['name']

class Trait(models.Model):
    name = models.CharField(max_length=500)
    desc = models.CharField("Description", max_length=900)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'trait_id': self.id})

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
