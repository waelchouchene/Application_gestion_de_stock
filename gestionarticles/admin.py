from django.contrib import admin
from .models import Article

# Register your models here.

@admin.register(Article)
class AuthorCategorie(admin.ModelAdmin):
    pass
