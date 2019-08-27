from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'pedidos'

router = routers.DefaultRouter()
router.register(r'pedidos', views.PedidosViewSet)
router.register(r'produtos', views.ProdutosViewSet)

urlpatterns = [
    # ex: /pedidos/
    path('', views.IndexView.as_view(), name='index'),
    path('api/', include(router.urls)),
]