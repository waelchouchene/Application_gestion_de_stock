from django.urls import path

from . import views

app_name = 'gestionclients'
urlpatterns = [
    path('clients', views.clients, name='clients'),
    path('ajouter_client', views.ajouter_client, name='ajouter_client'),
    path('modifier_client/(<id>[0-9]+)', views.modifier_client, name='modifier_client'),
    path('save_client/(<id>[0-9]+)', views.save_client, name='save_client'),
    path('delete_client/(<id>[0-9]+)', views.delete_client, name='delete_client'),
    path('affiche_commande_client/(<id>[0-9]+)', views.affiche_commande_client, name='affiche_commande_client'),

]
