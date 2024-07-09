from django.contrib import admin

from .models import Cargo, Servico, Funcionario, Post, Curso


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('topic', '_author')

    def _author(self, instance):
        return f'{instance.author.get_full_name()}'

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(author=request.user) #somente possibilita ver as proprias postagens

    exclude = ['author',]
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)  #impede de um usuario criar postagen com outro nome


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao', 'ativo')

