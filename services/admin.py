from django.contrib import admin

from .models import Service


class ServicesAdmin(admin.ModelAdmin):
    readonly_fields = ["created", "updated"]
    list_display = ("title", "subtitle")


admin.site.register(Service, ServicesAdmin)
