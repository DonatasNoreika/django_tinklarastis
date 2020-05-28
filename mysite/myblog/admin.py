from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Straipsnis

class StraipsnisAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'autorius', 'laikas', 'tekstas')

admin.site.register(Straipsnis, StraipsnisAdmin)