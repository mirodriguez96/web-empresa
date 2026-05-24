from django.db import models


class Service(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=200)
    subtitle = models.CharField(verbose_name="Subtitulo", max_length=200)
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateTimeField(verbose_name="Fecha de Creacion", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de actualizacion", auto_now=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["-created"]

    def __str__(self):
        return self.title
