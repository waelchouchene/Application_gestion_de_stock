from django.contrib import admin
from .models import DetailsCommande

# Register your models here.



@admin.register(DetailsCommande)
class AuthorDetailsCommande(admin.ModelAdmin):
    pass