from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from datetime import datetime


# Create your models here.

class Straipsnis(models.Model):
    pavadinimas = models.CharField('Pavadinimas', max_length=200)
    autorius = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    laikas = models.DateTimeField('Sukurta: ', null=True, blank=True, default=datetime.now)
    tekstas = HTMLField('Tekstas', null=True)

    @property
    def komentaru_skaicius(self):
        return len(Komentaras.objects.filter(straipsnis_id=self.pk))

    def __str__(self):
        return f"{self.pavadinimas} {self.autorius} {self.laikas}"

    class Meta:
        verbose_name = "Straipsnis"
        verbose_name_plural = "Straipsniai"


class Komentaras(models.Model):
    straipsnis_id = models.ForeignKey(Straipsnis, on_delete=models.SET_NULL, null=True, related_name='komentarai')
    vardas = models.CharField('Vardas', max_length=200)
    el_pastas = models.EmailField('El. paštas (nebūtina)', null=True, blank=True)
    laikas = models.DateTimeField('Sukurta: ', null=True, blank=True, default=datetime.now)
    komentaras = models.TextField("Komentaras")

    def __str__(self):
        return f"{self.vardas}, {self.laikas}: {self.komentaras}"

    class Meta:
        verbose_name = "Komentaras"
        verbose_name_plural = "Komentarai"