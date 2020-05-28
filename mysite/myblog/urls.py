from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('straipsniai/', views.StraipsnisListView.as_view(), name='straipsniai'),
    path('straipsniai/<int:pk>', views.StraipsnisDetailView.as_view(), name='straipsnis'),
]