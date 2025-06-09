from django.db import models

# Create your models here.
from django.utils import timezone

class ObraDeArte(models.Model):
    titulo = models.CharField(max_length=200)
    artista = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
