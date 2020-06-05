from django.shortcuts import render
from django.views import generic
from .models import Straipsnis
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


class StraipsnisListView(generic.ListView):
    model = Straipsnis
    template_name = 'straipsniai.html'
    paginate_by = 5
    ordering = ['-laikas']


class StraipsnisDetailView(generic.DetailView):
    model = Straipsnis
    template_name = 'straipsnis.html'


class StraipsnisCreateView(LoginRequiredMixin, generic.CreateView):
    model = Straipsnis
    fields = ['pavadinimas', 'tekstas']
    success_url = "/myblog/straipsniai/"
    template_name = 'straipsnis_form.html'

    def form_valid(self, form):
        form.instance.autorius = self.request.user
        return super().form_valid(form)


class StraipsnisUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Straipsnis
    fields = ['pavadinimas', 'tekstas']
    success_url = "/myblog/straipsniai/"
    template_name = 'straipsnis_form.html'

    def form_valid(self, form):
        form.instance.reader = self.request.user
        return super().form_valid(form)

    def test_func(self):
        straipnis = self.get_object()
        return self.request.user == straipnis.autorius