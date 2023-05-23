from django import forms
from .models import Pessoa


class CadastraPessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'cpf': 'CPF',
        }
