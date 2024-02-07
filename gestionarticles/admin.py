from django.contrib import admin
from .models import Categorie,Article

# Register your models here.

@admin.register(Categorie)
class AuthorCategorie(admin.ModelAdmin):
    pass
@admin.register(Article)
class AuthorCategorie(admin.ModelAdmin):
    pass
