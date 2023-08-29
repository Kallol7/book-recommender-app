from django.contrib import admin

from .models import Writer, Book

# Register your models here.
admin.site.register(Writer, list_distplay = ["name", "born"])
admin.site.register(Book, list_display = ["name", "writer", "year"])
