from django import forms
from django.forms import ModelForm

from .models import *


class TarefaForm(forms.ModelForm):

    class Meta:
        model = Tarefa
        fields = '__all__'
