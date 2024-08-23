from django import forms

class Formulario(forms.Form):
    
    nombre_curso = forms.CharField()
    camada_curso = forms.IntegerField()

    nombre_estudiante = forms.CharField()
    apellido_estudiante = forms.CharField()
    email_estudiante = forms.EmailField()

    nombre_profesor = forms.CharField()
    apellido_profesor = forms.CharField()
    email_profesor = forms.EmailField()

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=20)