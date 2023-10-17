from django.contrib import admin

from .models import Writer, Book
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(Writer, list_distplay = ["name", "born"])
admin.site.register(Book, list_display = ["name", "writer", "year"])
admin.site.register(User, UserAdmin, list_display = ["username", "email", "fullname"])
