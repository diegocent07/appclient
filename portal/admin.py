from django.contrib import admin

# Register your models here.

from .models import Datosclientes

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title', 'Docnro', 'email', 'Direcc', 'telefono', 'comprobantep')
    list_display_links = ('id', 'Title')
    search_fields = ('Title', 'Docnro','Direcc')
    list_per_page = 20
admin.site.register(Datosclientes, ClientesAdmin)
admin.site.site_header = "TOPDEK Clientes"
admin.site.site_title = "Lista de clientes"
admin.site.index_title = "Administración del sitio"
