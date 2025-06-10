from django.db import models
from django.utils import timezone

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def _str_(self):
        return self.titulo


class ObraArte(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateField()
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)

    def _str_(self):
        return self.titulo