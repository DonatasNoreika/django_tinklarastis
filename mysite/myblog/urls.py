from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('straipsniai/', views.StraipsnisListView.as_view(), name='straipsniai'),
    path('straipsniai/<int:pk>', views.StraipsnisDetailView.as_view(), name='straipsnis'),
    path('straipsniai/sukurti', views.StraipsnisCreateView.as_view(), name='straipsnis-sukurti'),
    path('straipsniai/<int:pk>/redaguoti', views.StraipsnisUpdateView.as_view(), name='straipsnis-redaguoti'),
]