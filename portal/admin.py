from django.contrib import admin

# Register your models here.

from .models import Datosclientes

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title', 'Direcc', 'comprobantep')
    list_display_links = ('id', 'Title')
    search_fields = ('Title', 'Direcc')
    list_per_page = 20
admin.site.register(Datosclientes, ClientesAdmin)