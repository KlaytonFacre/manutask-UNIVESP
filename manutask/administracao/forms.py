from django import forms
from .models import Pessoa, Imovel, Oficina, OrdemServico


class CadastraPessoaForm(forms.ModelForm):

    class Meta:
        model = Pessoa
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'cpf': 'CPF',
        }


class CadastraImovelForm(forms.ModelForm):

    class Meta:
        model = Imovel
        fields = '__all__'
        labels = {
            'id_locador': 'Locador',
            'rua': 'Rua',
            'numero': 'Número',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
        }


class CadastraOficinaForm(forms.ModelForm):

    class Meta:
        model = Oficina
        fields = '__all__'
        labels = {
            'id_supervisor': 'Supervisor',
            'nome': 'Nome',
        }


class CadastraOrdemServicoForm(forms.ModelForm):

    class Meta:
        model = OrdemServico
        fields = '__all__'
        exclude = [
            'timestamp_abertura',
            'timestamp_solucao',
            'descricao_solucao',
            'id_solucionador',
        ]
        labels = {
            'id_reclamante': 'Aberta por',
            'id_imovel': 'Imóvel afetado',
            'id_oficina_responsavel': 'Tipo de serviço',
            'descricao_problema': 'Descrição do problema',
        }