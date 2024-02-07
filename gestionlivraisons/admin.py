from django.contrib import admin
from .models import Livraison
# Register your models here.
@admin.register(Livraison)
class AuthorService(admin.ModelAdmin):
    pass
