from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('straipsniai/', views.StraipsnisListView.as_view(), name='straipsniai'),
    path('straipsniai/<int:pk>', views.StraipsnisDetailView.as_view(), name='straipsnis'),
    path('straipsniai/sukurti', views.StraipsnisCreateView.as_view(), name='straipsnis-sukurti'),
    path('straipsniai/<int:pk>/redaguoti', views.StraipsnisUpdateView.as_view(), name='straipsnis-redaguoti'),
    path('straipsniai/<int:pk>/istrinti', views.StraipsnisDeleteView.as_view(), name='straipsnis-istrinti'),
    path('komentaras/<int:pk>/', views.KomentarasUpdateView.as_view(), name='komentaras-redaguoti'),
    path('komentaras/<int:pk>/istrinti', views.KomentarasDeleteView.as_view(), name='komentaras-istrinti'),
]