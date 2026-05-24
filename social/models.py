from django.db import models


class Link(models.Model):
    # Caracteres alfanumericos, guines y barras y no deja usar caracteres especiales
    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Red social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(verbose_name="Fecha de Creacion", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de actualizacion", auto_now=True)

    class Meta:
        verbose_name = "Enlace"
        verbose_name_plural = "Enlaces"
        ordering = ["-name"]

    def __str__(self):
        return self.name
