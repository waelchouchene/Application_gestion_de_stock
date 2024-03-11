from django.contrib import admin
from .models import Personnel

# Register your models here.

@admin.register(Personnel)
class AuthorService(admin.ModelAdmin):
    pass
