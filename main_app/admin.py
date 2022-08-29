from django.contrib import admin
from .models import Champion, Trait, Augment, Video, TraitImage
# Register your models here.

admin.site.register(Champion)
admin.site.register(Trait)
admin.site.register(Augment)
admin.site.register(Video)
admin.site.register(TraitImage)