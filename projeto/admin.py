from django.contrib import admin
from projeto.models import Cliente  

class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'senha'),
    list_display_links = ('id', 'nome'),
    search_fields = ('nome', )

admin.site.register(Cliente, Clientes)
    
