from django.contrib import admin
from .models import Champion, Trait, Augment
# Register your models here.

admin.site.register(Champion)
admin.site.register(Trait)
admin.site.register(Augment)