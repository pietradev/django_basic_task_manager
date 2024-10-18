from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task #esse formulario é baseado no modelo Task de models.py
        fields = ['title', 'description', 'completed'] # campos exibidos no form