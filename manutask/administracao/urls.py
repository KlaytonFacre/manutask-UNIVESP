from django.urls import path
from .views import IndexTemplateView, PessoaListView, PessoaCreateView, PessoaUpdateView, \
    PessoaDeleteView, ImovelListView, ImovelUpdateView, ImovelDeleteView, ImovelCreateView, \
    OficinaListView, OficinaUpdateView, OficinaDeleteView, OficinaCreateView, \
    OrdemServicoListView, OrdemServicoUpdateView, OrdemServicoDeleteView, OrdemServicoCreateView

app_name = 'administracao'

urlpatterns = [
    # Homepage
    path('', IndexTemplateView.as_view(), name='index'),

    # Pessoas
    path('pessoas/', PessoaListView.as_view(), name='lista_pessoas'),
    path('pessoa/atualiza/<pk>', PessoaUpdateView.as_view(), name='atualiza_pessoa'),
    path('pessoa/excluir/<pk>', PessoaDeleteView.as_view(), name='deleta_pessoa'),
    path('pessoa/cadastrar', PessoaCreateView.as_view(), name='cadastra_pessoa'),

    # Imoveis
    path('imoveis/', ImovelListView.as_view(), name='lista_imoveis'),
    path('imovel/atualiza/<pk>', ImovelUpdateView.as_view(), name='atualiza_imovel'),
    path('imovel/excluir/<pk>', ImovelDeleteView.as_view(), name='deleta_imovel'),
    path('imovel/cadastrar', ImovelCreateView.as_view(), name='cadastra_imovel'),

    # Oficinas
    path('oficinas/', OficinaListView.as_view(), name='lista_oficinas'),
    path('oficina/atualiza/<pk>', OficinaUpdateView.as_view(), name='atualiza_oficina'),
    path('oficina/excluir/<pk>', OficinaDeleteView.as_view(), name='deleta_oficina'),
    path('oficina/cadastrar', OficinaCreateView.as_view(), name='cadastra_oficina'),

    # Ordens de Serviço
    path('os/', OrdemServicoListView.as_view(), name='lista_os'),
    path('os/atualiza/<pk>', OrdemServicoUpdateView.as_view(), name='atualiza_os'),
    path('os/excluir/<pk>', OrdemServicoDeleteView.as_view(), name='deleta_os'),
    path('os/cadastrar', OrdemServicoCreateView.as_view(), name='cadastra_os'),
]
