from django.contrib import admin
from .models import Fournisseur
# Register your models here.
@admin.register(Fournisseur)
class AuthorDetailsCommande(admin.ModelAdmin):
    pass
