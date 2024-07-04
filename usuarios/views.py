from django.shortcuts import render

from .models import ModelUsuario
# from .forms import ContatoForm


def loginuser(ModelUsuario):
    return render(ModelUsuario, 'logindex.html')
