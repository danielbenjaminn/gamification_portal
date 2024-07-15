from django import forms
from django.contrib import admin
from .models import Desafio, DesafioAtribuido, Pontuacao
from accounts.models import User

class DesafioAtribuidoForm(forms.ModelForm):
    class Meta:
        model = DesafioAtribuido
        fields = ['desafio', 'corretor']  # Excluir os campos aceito e data_interacao

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar usuários que não são superusers ou staff
        self.fields['corretor'].queryset = User.objects.filter(is_superuser=False, is_staff=False)

class DesafioAtribuidoAdmin(admin.ModelAdmin):
    form = DesafioAtribuidoForm
    list_display = ('desafio', 'corretor')  # Remover aceito e data_interacao da exibição

admin.site.register(Desafio)
admin.site.register(DesafioAtribuido, DesafioAtribuidoAdmin)
admin.site.register(Pontuacao)
