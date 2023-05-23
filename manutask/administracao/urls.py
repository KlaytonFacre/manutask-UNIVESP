from django.urls import path
from .views import IndexTemplateView, PessoaListView, PessoaCreateView, PessoaUpdateView, \
    PessoaDeleteView


app_name = 'administracao'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('pessoas/', PessoaListView.as_view(), name='lista_pessoas'),
    path('pessoa/atualiza/<pk>', PessoaUpdateView.as_view(), name='atualiza_pessoa'),
    path('pessoa/excluir/<pk>', PessoaDeleteView.as_view(), name='deleta_pessoa'),
    path('pessoa/cadastrar', PessoaCreateView.as_view(), name='cadastra_pessoa'),
]