from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'pedidos'

router = routers.DefaultRouter()
router.register(r'pedidos', views.PedidosViewSet, 'pedido') #quando a view usa o get_queryset é obrigatório o basename
router.register(r'produtos', views.ProdutosViewSet, 'produto')
router.register(r'itens', views.ItemPedidoViewSet)
router.register(r'categorias', views.CategoriaViewSet)

urlpatterns = [
    # ex: /pedidos/
    path('', views.IndexView.as_view(), name='index'),
    path('api/', include(router.urls)),
]