
from django.urls import path
# from .views import hola, hola2, fecha_actual
# from ..home import views
from home import views
# from . import views

urlpatterns = [
    path('',views.index),
    # path('hola/', views.hola),
    # path('Hola2/', views.hola2),
    # path('fecha-actual/', views.fecha_actual),
    # path('fecha-nacimiento/<int:edad>', views.calcular_fecha_nacimiento),
    # path('mi-template/', views.mi_template),
    # path('mi-template/<str:nombre>', views.segundo_template),
    # path('tercer-template/', views.tercer_template),
    path('ver-personas/', views.ver_personas),
    path('crear-persona/<str:nombre>/<str:apellido>/', views.crear_persona),
    # path('hola/', hola),
    # path('Hola2/', hola2),
    # path('fecha-actual/', fecha_actual),
    #path('crear-persona/', views.crear_persona), # REV 07/10/22
    # path('crear-familiar/<str:nombre>/<str:apellido>/', views.crear_familiar), 
    path('crear-familiar/', views.crear_familiar), 
    path('ver-familiar/', views.ver_familiar), 
]