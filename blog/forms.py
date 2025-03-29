from django import forms
from .models import Comentario, Seguidor

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre', 'correo', 'contenido']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-pink-300 rounded-lg shadow-sm focus:ring-pink-500 focus:border-pink-500',
                'placeholder': 'Tu nombre'
            }),
            'correo': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-pink-300 rounded-lg shadow-sm focus:ring-pink-500 focus:border-pink-500',
                'placeholder': 'Tu nombre'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'w-full p-3 border border-pink-300 rounded-lg shadow-sm focus:ring-pink-500 focus:border-pink-500',
                'placeholder': 'Escribe tu comentario...',
                'rows': 4
            }),
        }

class SeguidorForm(forms.ModelForm):
    class Meta:
        model = Seguidor
        fields = ['correo']
        widgets = {
            'correo': forms.EmailInput(attrs={'placeholder': 'Ingrese su correo electrónico'}),
        }
        widgets = {
            'correo': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-pink-300 rounded-lg shadow-sm focus:ring-pink-500 focus:border-pink-500',
                'placeholder': 'Tu nombre'
            }),
        }
        labels = {
            'correo': 'Correo electrónico',
        }