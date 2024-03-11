from django.contrib import admin
from .models import DetailsCommande,Commande

# Register your models here.



@admin.register(DetailsCommande)
class AuthorDetailsCommande(admin.ModelAdmin):
    pass

@admin.register(Commande)
class AuthorDetailsCommande(admin.ModelAdmin):
    pass