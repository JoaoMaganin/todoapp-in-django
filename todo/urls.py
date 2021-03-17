from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('atualizar-tarefa/<str:pk>/', atualizar_tarefa, name='atualizar_tarefa'),
    path('deletar-tarefa/<str:pk>/', deletar_tarefa, name='deletar_tarefa'),
]
