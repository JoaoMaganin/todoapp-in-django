from django.db import models


class Tarefa(models.Model):
    titulo = models.CharField('Título', max_length=20)
    completo = models.BooleanField('Completo?', default=False)
    data_criado = models.DateTimeField('Data de criação', auto_now_add=True)

    def __str__(self):
        return self.titulo
