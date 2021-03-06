from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
#https://docs.djangoproject.com/en/2.1/topics/auth/default/
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_condition import Or
from django_filters import rest_framework as filters
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication

from .serializers import PedidosSerializer, ProdutosSerializer, ItemPedidoSerializer, CategoriaSerializer, AdicionalSerializer
from .models import Produto, Pedido, Categoria, Adicional, ItemPedido
# Create your views here.

class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/admin/login/'

    model = Produto
    template_name = 'pedidos/index.html'
    context_object_name = 'produtos_list'


class ProdutosViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        return Produto.objects.filter(indisponivel=False)

    serializer_class = ProdutosSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('nome', 'Descrição')


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class PedidosViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Pedido.objects.filter(cliente=self.request.user).order_by('-data')

    serializer_class = PedidosSerializer
    # Tipos de autenticação suportados. OAuth2 para rest, Session para uso via browser
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class ItemPedidoViewSet(viewsets.ModelViewSet):
    serializer_class = ItemPedidoSerializer
    queryset = ItemPedido.objects.all()
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('pedido',)


class AdicionalViewSet(viewsets.ModelViewSet):
    serializer_class = AdicionalSerializer
    queryset = Adicional.objects.all()
#    authentication_classes = [OAuth2Authentication, SessionAuthentication]
#    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'
