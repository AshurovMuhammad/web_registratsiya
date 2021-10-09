from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sarlavhani kiriting'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tavsifni kiriting'
            }),
        }
