from django.contrib import admin
from .models import Item, Cliente, Inventario


class InventarioAdmin(admin.ModelAdmin):
    list_display = ('Dono', 'Carta')
    list_filter = ('Dono', 'Carta')

admin.site.register(Item)
admin.site.register(Cliente)
admin.site.register(Inventario, InventarioAdmin)