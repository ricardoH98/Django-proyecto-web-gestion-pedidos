from django.db import models

# Create your models here.
class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to= 'servicios')
    created = models.DateTimeField(auto_now= True)
    updated = models.DateTimeField(auto_now= True)

    class Meta:
        verbose_name = 'servicio de la app'
        verbose_name_plural = 'servicios varios'

    def __str__(self):
        return self.titulo