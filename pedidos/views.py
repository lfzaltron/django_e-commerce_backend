from django.shortcuts import render
from django.views import generic

from .models import Produto
# Create your views here.

class IndexView(generic.ListView):
    model = Produto
    template_name = 'pedidos/index.html'
    context_object_name = 'produtos_list'
