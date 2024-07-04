from django.urls import path
from .views import IndexView
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cursos/', views.cursos_view, name='cursos'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('login/', views.login_view, name='login'),
]
