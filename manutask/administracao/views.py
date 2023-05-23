from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, \
    DeleteView
from .models import Pessoa
from .forms import CadastraPessoaForm


# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'administracao/index.html'


class PessoaListView(ListView):
    template_name = 'administracao/listapessoas.html'
    model = Pessoa
    context_object_name = 'pessoas'


class PessoaUpdateView(UpdateView):
    template_name = 'administracao/atualizapessoa.html'
    model = Pessoa
    fields = '__all__'
    context_object_name = 'pessoa'
    success_url = reverse_lazy('administracao:lista_pessoas')


class PessoaDeleteView(DeleteView):
    template_name = 'administracao/deletapessoa.html'
    model = Pessoa
    context_object_name = 'pessoa'
    success_url = reverse_lazy('administracao:lista_pessoas')


class PessoaCreateView(CreateView):
    template_name = 'administracao/cadastrapessoa.html'
    model = Pessoa
    form_class = CadastraPessoaForm
    success_url = reverse_lazy('administracao:lista_pessoas')
