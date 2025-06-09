from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from .models import ObraDeArte

def lista_obras(request):
    obras = ObraDeArte.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_creacion')
    return render(request, 'museo/lista_obras.html', {'obras': obras})
