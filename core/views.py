from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render
from .models import Servico, Funcionario, Curso
from .forms import ContatoForm


def cursos_view(request):
    order_by = request.GET.get('order_by', 'criado_em')
    cursos = Curso.objects.all().order_by(order_by)[:20]
    return render(request, 'cursos.html', {'cursos': cursos})

def perfil_view(request):
    return render(request, 'viewperfil.html')


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.all()
        #context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o e-mail.')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
