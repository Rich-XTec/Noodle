from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ModelUsuario

class ModelUsuarioCreateForm(UserCreationForm):
    class Meta:
        model = ModelUsuario
        fields = ('username', 'first_name')
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False) #salvar a variavel, mas ainda não no banco
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]

        if commit:
            user.save()
        return user

class ModelUsuarioChangeForm(UserChangeForm):
    class Meta:
        model = ModelUsuario
        fields = ('first_name', 'last_name', 'fone')
