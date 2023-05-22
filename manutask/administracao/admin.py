from django.contrib import admin
from .models import Pessoa, Oficina, Imovel, OrdemServico

# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Oficina)
admin.site.register(Imovel)
admin.site.register(OrdemServico)
