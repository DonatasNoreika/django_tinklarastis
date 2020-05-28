from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Straipsnis(models.Model):
    pavadinimas = models.CharField('Pavadinimas', max_length=200)
    autorius = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    laikas = models.DateTimeField('Sukurta: ', null=True, blank=True)
    tekstas = HTMLField('Tekstas', null=True)

    def __str__(self):
        return f"{self.pavadinimas} {self.autorius} {self.laikas}"