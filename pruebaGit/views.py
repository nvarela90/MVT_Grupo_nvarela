from django.http import HttpResponse


def hola(request):
    return HttpResponse('<h1>Esto es nuevo</h1>')

def hola2(request):
    return HttpResponse('<h1>Esto es el hola 2</h1>')