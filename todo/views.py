from django.shortcuts import render
from .models import Tarefa

from .forms import *


def index(request):
    tarefas = Tarefa.objects.all()

    form = TarefaForm()

    context = {
        'tarefas': tarefas,
        'form': form,
    }

    return render(request, 'index.html', context)
