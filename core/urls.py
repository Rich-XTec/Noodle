from django.urls import path
from . import views
from .views import IndexView, CursosView, perfil_view


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cursos/', CursosView.as_view(), name='cursos'),
    path('perfil/', views.perfil_view, name='perfil'),
]
