from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import loginuser

urlpatterns = [
    #path('', TemplateView.as_view(template_name='logindex.html'), name='logindex'),
    path('', loginuser),
    path('contas/', include('django.contrib.auth.urls')) #rotas de autenticação do django
]