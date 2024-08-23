from django.urls import path
from Web import views

urlpatterns = [
    path('',views.inicio, name = 'inicio'),
    path('vista_cursos/',views.cursos, name = 'curso'),
    path('vista_estudiante/',views.estudiante, name = 'estudiante'),
    path('vista_profesores/',views.profesores, name = 'profesores'),
    path('pagina_Formulario/',views.paginaFormulario, name = 'Formulario de Página'),
    path('busqueda_Camada/', views.busquedaCamada, name = 'busquedaCamada'),
    path('buscar/', views.buscar),
]