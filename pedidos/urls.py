from django.urls import path
from . import views

app_name = 'pedidos'
urlpatterns = [
    # ex: /pedidos/
    path('', views.IndexView.as_view(), name='index'),
]