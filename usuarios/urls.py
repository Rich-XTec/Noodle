from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('contas/', include('django.contrib.auth.urls')) #rotas de autenticação do django
]