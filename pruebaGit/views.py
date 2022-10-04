from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader 

def hola(request):
    return HttpResponse('<h1>Esto es nuevo</h1>')

def hola2(request):
    return HttpResponse('<h1>Esto es el hola 2</h1>')

def fecha_actual(request):
    fecha_ahora = datetime.now()
    return HttpResponse(f'La fecha y hora actual es {fecha_ahora}')

def calcular_fecha_nacimiento(request, edad):
    
    fecha = datetime.now().year - edad
    
    return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} años sería: {fecha}')

def mi_template(request):
    
    cargar_file = open(r'C:\Users\nicoo\OneDrive\Escritorio\Proyecto-python\templates\template.html', 'r')
    template = Template(cargar_file.read())
    cargar_file.close()
    contexto = Context()
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)

def segundo_template(request, nombre):
    
    # cargar_file = open(r'C:\Users\nicoo\OneDrive\Escritorio\Proyecto-python\templates\segundo_template.html', 'r')
    # template = Template(cargar_file.read())
    # cargar_file.close()
    # contexto = Context({'persona':nombre})
    # template_renderizado = template.render(contexto)
    # return HttpResponse(template_renderizado)

    template = loader.get_template('segundo_template.html')
    template_renderizado = template.render({'persona': nombre})
    return HttpResponse(template_renderizado)
    
    