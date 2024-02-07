from django.contrib import admin
from .models import Service, Personnel

# Register your models here.

@admin.register(Service)
class AuthorService(admin.ModelAdmin):
    pass

@admin.register(Personnel)
class AuthorService(admin.ModelAdmin):
    pass
