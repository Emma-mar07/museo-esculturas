from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion #se importan las publicaciones
from django.contrib.auth.models import User #se importan los usuarios 

# Create your views here.
def lista_public(request):
    publicaciones=Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion') #se filtran las publicaciones con fecha de publicacion

    usr_id=request.GET.get('usuario') #usr_id se guarda el usuario
    if usr_id:
        publicaciones=publicaciones.filter(autor__id=usr_id) #agrego un filtro
    
    usuarios=User.objects.all() #traigo todos los usuarios y los guardo en usuarios
    if usr_id: #usuario activo?
        usuario_activo = int(usr_id) #se pinta el usuario seleccionado se pasa una variable como entera
    else:
        usuario_activo = None

    return render(request, 'blog/lista_public.html', { #retorno las librerias
        'publicaciones':publicaciones,
        'usuarios':usuarios,
        'usuario_activo':usuario_activo
    })