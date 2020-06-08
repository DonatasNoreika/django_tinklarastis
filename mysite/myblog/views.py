from django.shortcuts import render, reverse
from django.views import generic
from .models import Straipsnis, Komentaras
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin
from .forms import KomentarasForm

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


class StraipsnisListView(generic.ListView):
    model = Straipsnis
    template_name = 'straipsniai.html'
    paginate_by = 5
    ordering = ['-laikas']


class StraipsnisDetailView(FormMixin, generic.DetailView):
    model = Straipsnis
    template_name = 'straipsnis.html'
    form_class = KomentarasForm

    def get_success_url(self):
        return reverse('straipsnis', kwargs={'pk': self.object.id})

    def get_context_data(self, *args, **kwargs):
        context = super(StraipsnisDetailView, self).get_context_data(**kwargs)
        context['form'] = KomentarasForm(initial={'straipsnis_id': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.straipsnis_id = self.object
        form.instance.komentatorius = self.request.user
        form.save()
        return super(StraipsnisDetailView, self).form_valid(form)


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

class StraipsnisDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Straipsnis
    success_url = "/myblog/straipsniai/"
    template_name = 'straipsnis_delete.html'

    def form_valid(self, form):
        form.instance.reader = self.request.user
        return super().form_valid(form)

    def test_func(self):
        straipnis = self.get_object()
        return self.request.user == straipnis.autorius

class KomentarasUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Komentaras
    fields = ['vardas', 'el_pastas', 'komentaras']
    success_url = "/myblog/straipsniai/"
    template_name = 'komentaras_form.html'

    def test_func(self):
        komentaras = self.get_object()
        return self.request.user == komentaras.komentatorius


class KomentarasDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Komentaras
    success_url = "/myblog/straipsniai/"
    template_name = 'komentaras_delete.html'

    def test_func(self):
        komentaras = self.get_object()
        return self.request.user == komentaras.komentatorius