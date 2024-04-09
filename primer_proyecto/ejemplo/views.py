from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def ejemplo(request):
    return HttpResponse("Hola mundo")

def gato(request):
    return HttpResponse("hola denuevo")

def about(request):
    return HttpResponse("vista about")

def contact(request):
    return HttpResponse("""
       <h1>Vista para el Contacto</h1>
       <form action="/contacto" method="">
           <input type="text" name="nombre" placeholder="Nombre">
           <input type="email" name="correo" placeholder="Correo electrónico">
           <textarea name="mensaje" placeholder="Mensaje"></textarea>
           <input type="submit" value="Enviar">
                        </form> """)

def home(request):
    return HttpResponse("""
       <h1>Ejemplo de aplicación web con múltiples vistas!!!</h1>
       <p>Esta es mi primera aplicación con Django mostrando HTML</p>
       <img src="https://picsum.photos/200/300" />
       """)