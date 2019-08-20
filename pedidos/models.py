from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField(max_length=400, name='Descrição')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='produtos/', default='pic_folder/None/no-img.jpg')

    def __str__(self):
        return self.nome