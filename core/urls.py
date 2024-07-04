from django.urls import path
from . import views
from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cursos/', views.cursos_view, name='cursos'),
    path('perfil/', views.perfil_view, name='perfil'),
]
