from django import forms
from .models import ToDo

class Form(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ["item", "completed"]