from django.shortcuts import render, redirect
from .models import Tarefa

from .forms import *


def index(request):
    tarefas = Tarefa.objects.all()

    form = TarefaForm()

    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'tarefas': tarefas,
        'form': form,
    }

    return render(request, 'index.html', context)


def atualizar_tarefa(request, pk):
    tarefa = Tarefa.objects.get(id=pk)

    form = TarefaForm(instance=tarefa)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }

    return render(request, 'atualizar_tarefa.html', context)


def deletar_tarefa(request, pk):
    item = Tarefa.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('index')

    context = {
        'item': item
    }

    return render(request, 'deletar_tarefa.html', context)