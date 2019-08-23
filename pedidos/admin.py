from django.contrib import admin

from .models import Produto, Pedido, ItemPedido

# Register your models here.
class ItemPodidoInline(admin.StackedInline):
    model = ItemPedido


class PedidosAdmin(admin.ModelAdmin):
    inlines = [ItemPodidoInline]
    list_display = ('data', 'quantidade_itens')

admin.site.register(Produto)
admin.site.register(Pedido, PedidosAdmin)
#admin.site.register(ItemPedido)