from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, \
    DeleteView
from .models import Pessoa, Imovel, Oficina, OrdemServico
from .forms import CadastraPessoaForm, CadastraImovelForm, CadastraOficinaForm, \
    CadastraOrdemServicoForm


# View da Homepage
class IndexTemplateView(TemplateView):
    template_name = 'administracao/index.html'


# Views da entidade Pessoa
class PessoaListView(ListView):
    template_name = 'administracao/pessoa/listapessoas.html'
    model = Pessoa
    context_object_name = 'pessoas'


class PessoaUpdateView(UpdateView):
    template_name = 'administracao/pessoa/atualizapessoa.html'
    model = Pessoa
    fields = '__all__'
    context_object_name = 'pessoa'
    success_url = reverse_lazy('administracao:lista_pessoas')


class PessoaDeleteView(DeleteView):
    template_name = 'administracao/pessoa/deletapessoa.html'
    model = Pessoa
    context_object_name = 'pessoa'
    success_url = reverse_lazy('administracao:lista_pessoas')


class PessoaCreateView(CreateView):
    template_name = 'administracao/pessoa/cadastrapessoa.html'
    model = Pessoa
    form_class = CadastraPessoaForm
    success_url = reverse_lazy('administracao:lista_pessoas')


# Views da entidade Imoveis
class ImovelListView(ListView):
    template_name = 'administracao/imovel/listaimoveis.html'
    model = Imovel
    context_object_name = 'imoveis'


class ImovelUpdateView(UpdateView):
    template_name = 'administracao/imovel/atualizaimovel.html'
    model = Imovel
    fields = '__all__'
    context_object_name = 'imovel'
    success_url = reverse_lazy('administracao:lista_imoveis')


class ImovelDeleteView(DeleteView):
    template_name = 'administracao/imovel/deletaimovel.html'
    model = Imovel
    context_object_name = 'imovel'
    success_url = reverse_lazy('administracao:lista_imoveis')


class ImovelCreateView(CreateView):
    template_name = 'administracao/imovel/cadastraimovel.html'
    model = Imovel
    form_class = CadastraImovelForm
    success_url = reverse_lazy('administracao:lista_imoveis')


# Views da entidade Oficina
class OficinaListView(ListView):
    template_name = 'administracao/oficina/listaoficinas.html'
    model = Oficina
    context_object_name = 'oficinas'


class OficinaUpdateView(UpdateView):
    template_name = 'administracao/oficina/atualizaoficina.html'
    model = Oficina
    fields = '__all__'
    context_object_name = 'oficina'
    success_url = reverse_lazy('administracao:lista_oficinas')


class OficinaDeleteView(DeleteView):
    template_name = 'administracao/oficina/deletaoficina.html'
    model = Oficina
    context_object_name = 'oficina'
    success_url = reverse_lazy('administracao:lista_oficinas')


class OficinaCreateView(CreateView):
    template_name = 'administracao/oficina/cadastraoficina.html'
    model = Oficina
    form_class = CadastraOficinaForm
    success_url = reverse_lazy('administracao:lista_oficinas')


# Views da entidade OrdemServico
class OrdemServicoListView(ListView):
    template_name = 'administracao/ordemservico/listaordensservico.html'
    model = OrdemServico
    context_object_name = 'ordensservico'


class OrdemServicoUpdateView(UpdateView):
    template_name = 'administracao/ordemservico/atualizaordemservico.html'
    model = OrdemServico
    fields = '__all__'
    context_object_name = 'os'
    success_url = reverse_lazy('administracao:lista_os')


class OrdemServicoDeleteView(DeleteView):
    template_name = 'administracao/ordemservico/deletaordemservico.html'
    model = OrdemServico
    context_object_name = 'os'
    success_url = reverse_lazy('administracao:lista_os')


class OrdemServicoCreateView(CreateView):
    template_name = 'administracao/ordemservico/cadastraordemservico.html'
    model = OrdemServico
    form_class = CadastraOrdemServicoForm
    success_url = reverse_lazy('administracao:lista_os')

