from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
#https://docs.djangoproject.com/en/2.1/topics/auth/default/
from rest_framework import viewsets
from .serializers import PedidosSerializer, ProdutosSerializer

from .models import Produto, Pedido, Categoria
# Create your views here.

class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/admin/login/'

    model = Produto
    template_name = 'pedidos/index.html'
    context_object_name = 'produtos_list'


# https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/
class PedidosViewSet(viewsets.ModelViewSet):
    login_url = '/admin/login/'
    queryset = Pedido.objects.all().order_by('-data')
    serializer_class = PedidosSerializer


class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutosSerializer
