from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
#https://docs.djangoproject.com/en/2.1/topics/auth/default/

from .models import Produto
# Create your views here.

class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/admin/login/'

    model = Produto
    template_name = 'pedidos/index.html'
    context_object_name = 'produtos_list'
