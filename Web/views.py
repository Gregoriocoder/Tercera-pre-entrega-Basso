from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(req):
    return render(req, "web/index.html")

def cursos(req):
    return render(req, "web/cursos.html")

def estudiante(req):
    return render(req, "web/estudiante.html")

def profesores(req):
    return render(req, "web/profesores.html")

from django.shortcuts import render
from Web.forms import Formulario
from Web.models import Curso, Estudiante, Profesor

def paginaFormulario(request):
    if request.method == "POST":  # Si el formulario fue enviado
        miFormulario = Formulario(request.POST)  # Creamos un objeto formulario con los datos enviados
        print(miFormulario)  # Imprimimos el formulario para depuración (opcional)

        if miFormulario.is_valid():  # Verificamos si los datos son válidos
            informacion = miFormulario.cleaned_data  # Obtenemos los datos limpios y validados
            curso = Curso(nombre=informacion["nombre_curso"], camada=informacion["camada_curso"])  # Creamos un objeto Curso
            curso.save()  # Guardamos el curso en la base de datos

            estudiante = Estudiante(nombre=informacion["nombre_estudiante"], apellido=informacion["apellido_estudiante"], email=informacion["email_estudiante"])  # Creamos un objeto Curso
            estudiante.save()  # Guardamos el curso en la base de datos

            profesor = Profesor(nombre=informacion["nombre_profesor"], apellido=informacion["apellido_profesor"], email=informacion["email_profesor"])  # Creamos un objeto Curso
            profesor.save()  # Guardamos el curso en la base de datos
            
            return render(request, "web/index.html")  # Redirigimos a la página de inicio
    else:
        miFormulario = Formulario()  # Creamos un formulario vacío para mostrarlo inicialmente

    return render(request, "web/cursoFormulario.html", {"miFormulario": miFormulario})

def busquedaCamada(request):
    return render(request, 'web/busquedaCamada.html')

def buscar(request):
    if request.GET['camada']:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, 'web/resultadoBusqueda.html', {"cursos": cursos, "camada": camada})
    
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)
