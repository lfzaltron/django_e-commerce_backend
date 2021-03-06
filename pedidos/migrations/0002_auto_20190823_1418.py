# Generated by Django 2.1 on 2019-08-23 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=1)),
                ('observacao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Carrinho'), (1, 'Aguardando confirmação do restaurante'), (2, 'Confirmado'), (3, 'Em produção'), (4, 'Aguardando retirada'), (5, 'Finalizado')], default=0)),
                ('data', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='itempedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Pedido'),
        ),
        migrations.AddField(
            model_name='itempedido',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Produto'),
        ),
    ]
