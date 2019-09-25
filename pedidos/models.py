from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(max_length=400, name='Descrição')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='produtos/', default='pic_folder/None/no-img.jpg')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    indisponivel = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    # utilizado já para carrinho de compras? acho que sim
    STATUS_PEDIDO = (
        (0, 'Carrinho'),
        (1, 'Aguardando confirmação do restaurante'),
        (2, 'Confirmado'),
        (3, 'Em produção'),
        (4, 'Aguardando retirada'),
        (5, 'Finalizado'),
    ) # https://stackoverflow.com/questions/12725720/django-choices-how-to-set-default-option
    status = models.IntegerField(null=False, choices=STATUS_PEDIDO, default=0)
    cliente = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # forma de pagamento
    data = models.DateTimeField() # DataHora da CONFIRMAÇÃO do pedido.

    def __str__(self):
        return str(self.data)

    def quantidade_itens(self):
        itens = ItemPedido.objects.filter(pedido=self)
        return sum(map(lambda x: x.quantidade, itens))


class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    #adicionais =
    #remover?
    observacao = models.CharField(max_length=200, blank=True)

class Adicional(models.Model):
    nome = models.CharField(max_length=60)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    #Avaliar a possibilidade de por uma categoria aqui.. aí teria adicionais de panqueca doce, salgada, etc.


#Não esquecer dos testes