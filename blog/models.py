from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=100)
    created = models.DateTimeField(verbose_name="Fecha de Creacion", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de actualizacion", auto_now=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=200)
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicacion", default=now)
    image = models.ImageField(
        verbose_name="Imagen", upload_to="blog", null=True, blank=True
    )
    author = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)

    # related_name, para definir cual es el nombre de la relacion
    categories = models.ManyToManyField(
        Category, verbose_name="Categorias", related_name="get_post"
    )

    created = models.DateTimeField(verbose_name="Fecha de Creacion", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de actualizacion", auto_now=True)

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ["-created"]

    def __str__(self):
        return self.title
