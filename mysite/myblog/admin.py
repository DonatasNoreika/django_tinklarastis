from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Straipsnis, Komentaras

class KomentarasInline(admin.TabularInline):
    model = Komentaras

class StraipsnisAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'autorius', 'laikas', 'tekstas')
    inlines = [KomentarasInline]

class KomentarasAdmin(admin.ModelAdmin):
    list_display = ('straipsnis_id', 'komentatorius', 'vardas', 'el_pastas', 'laikas', 'komentaras')

admin.site.register(Straipsnis, StraipsnisAdmin)
admin.site.register(Komentaras, KomentarasAdmin)