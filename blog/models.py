from django.conf import settings
from django.db import models
from django.utils import timezone

class Publicacion(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    
    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()
        
    def __str__(self):
        return self.titulo
    
class ObraArte (models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField()
    imagen = models.ImageField(upload_to="imagenes/", blank=True, null=True)
    
    def __str__(self):
        return self.titulo
