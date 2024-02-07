from django.urls import path

from . import views

app_name = 'gestionfournisseurs'
urlpatterns = [
    path('fournisseurs', views.fournisseurs, name='fournisseurs'),
    path('ajouter_fournisseur', views.ajouter_fournisseur, name='ajouter_fournisseur'),
    path('modifier_fournisseur/(<id>[0-9]+)', views.modifier_fournisseur, name='modifier_fournisseur'),
    path('save_fournisseur/(<id>[0-9]+)', views.save_fournisseur, name='save_fournisseur'),
    path('delete_fournisseur/(<id>[0-9]+)', views.delete_fournisseur, name='delete_fournisseur'),

]
