from django.contrib import admin

from .models import Produto, Pedido, ItemPedido, Categoria

# Register your models here.
class ItemPodidoInline(admin.StackedInline):
    model = ItemPedido


class PedidosAdmin(admin.ModelAdmin):
    inlines = [ItemPodidoInline]
    list_display = ('data', 'quantidade_itens')


class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'Descrição','categoria', 'valor')


admin.site.register(Produto, ProdutosAdmin)
admin.site.register(Pedido, PedidosAdmin)
admin.site.register(Categoria)