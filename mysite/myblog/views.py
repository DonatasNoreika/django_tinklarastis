from django.shortcuts import render
from django.views import generic
from .models import Straipsnis

# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

class StraipsnisListView(generic.ListView):
    model = Straipsnis
    template_name = 'straipsniai.html'
    paginate_by = 5

class StraipsnisDetailView(generic.DetailView):
    model = Straipsnis
    template_name = 'straipsnis.html'