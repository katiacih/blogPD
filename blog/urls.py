"""Usando regex
^ para o início do texto
$ para o final do texto
\d para um dígito
r significa expressao regular
+ para indicar que o item anterior deve ser repetido pelo menos uma vez
() para capturar parte do padrão
"""

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #path(r'^/$', views.post_list, name='post_list'),
    path('post_list', views.post_list, name='post_list'),

]
