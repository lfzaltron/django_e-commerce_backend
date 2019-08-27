from rest_framework import serializers
from.models import Produto, Pedido

class PedidosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pedido
        fields = ['data', 'status']


class ProdutosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produto
        fields = ['nome', 'Descrição', 'valor', 'indisponivel', 'foto']
