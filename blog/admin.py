from django.contrib import admin
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ["created", "updated"]
    list_display = ("name",)


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ["created", "updated"]
    list_display = ("title", "author", "published", "get_categories")
    ordering = ("author", "published")

    # Busqueda de autor se debe hacer asi porque es una relacion a modelo, hay que especificar
    # que queremos buscar
    search_fields = ("title", "author__username", "categories__name")

    # Orden por fechas - se hace mas limpio buscar asi
    date_hierarchy = "published"

    # Agregar filtro de busqueda
    list_filter = ("author__username", "categories__name")

    def get_categories(self, object):
        return ", ".join([c.name for c in object.categories.all().order_by("name")])

    get_categories.short_description = "Categorias"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
