from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader 
import random
from home.models import Persona, Familiar

# def hola(request):
#     return HttpResponse('<h1>Esto es nuevo</h1>')

# def hola2(request):
#     return HttpResponse('<h1>Esto es el hola 2</h1>')

# def fecha_actual(request):
#     fecha_ahora = datetime.now()
#     return HttpResponse(f'La fecha y hora actual es {fecha_ahora}')

# def calcular_fecha_nacimiento(request, edad):
    
#     fecha = datetime.now().year - edad
    
#     return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} años sería: {fecha}')

# def mi_template(request):
    
#     cargar_file = open(r'C:\Users\nicoo\OneDrive\Escritorio\Proyecto-python\templates\template.html', 'r')
#     template = Template(cargar_file.read())
#     cargar_file.close()
#     contexto = Context()
#     template_renderizado = template.render(contexto)
    
#     return HttpResponse(template_renderizado)

# def segundo_template(request, nombre):
    
#     # cargar_file = open(r'C:\Users\nicoo\OneDrive\Escritorio\Proyecto-python\templates\segundo_template.html', 'r')
#     # template = Template(cargar_file.read())
#     # cargar_file.close()
#     # contexto = Context({'persona':nombre})
#     # template_renderizado = template.render(contexto)
#     # return HttpResponse(template_renderizado)

#     template = loader.get_template('segundo_template.html')
#     template_renderizado = template.render({'persona': nombre})
#     return HttpResponse(template_renderizado)


# def tercer_template(request):
    
#     mi_contexto = {
#         'rango': list(range(1,11)),
#         'valor_aleatorio': random.randrange(1,11)
#         }

#     template = loader.get_template('tercer_template.html')
#     template_renderizado = template.render(mi_contexto)
#     return HttpResponse(template_renderizado)
  
 #[[[[[PRIMERA ENTREGA]]]]]   
# def crear_persona(request,nombre,apellido):
#     persona = Persona(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
#     # persona1 = Persona(nombre='Diego', apellido='Maradona', edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
#     # persona2 = Persona(nombre='Román', apellido='Riquelme', edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
#     # persona3 = Persona(nombre='Roberto', apellido='Carlos', edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
#     persona.save() #Para que guarde en la db la persona creada.
#     # persona1.save()
#     # persona2.save()
#     # persona3.save()
#     template = loader.get_template('crear_persona.html')
#     template_renderizado = template.render({'persona':persona})
       
#     return HttpResponse()
    
#[[[REV 1 07/10/22]]]

# def crear_persona(request):
#      template = loader.get_template('crear_persona.html')
#      template_renderizado = template.render()
#      return HttpResponse(template_renderizado) 


    
# def ver_personas(request):
    
#     personas = Persona.objects.all() 
#     template = loader.get_template('ver_personas.html')
#     template_renderizado = template.render({'personas': personas})
#     return HttpResponse(template_renderizado)


#[[[REV 2 07/10/22]]]

def crear_familiar(request):
    # familiar = Familiar(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
    # familiar.save()
    # familiar = Familiar(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
    familiar1 = Familiar(nombre='Diego', apellido='Maradona', edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
    familiar2 = Familiar(nombre='Román', apellido='Riquelme', edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
    familiar3 = Familiar(nombre='Roberto', apellido='Carlos', edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
    familiar1.save()
    familiar2.save()
    familiar3.save()
    
    template = loader.get_template('crear_familiar.html')
    template_renderizado = template.render()
    
    return HttpResponse(template_renderizado) 

def ver_familiar(request):
    
    familiar = Familiar.objects.all()
    
    template = loader.get_template('ver_familiar.html')
    template_renderizado = template.render({'familiar': familiar})
    
    return HttpResponse(template_renderizado) 