from django.urls import path

from . import views

app_name = 'gestioncommandes'
urlpatterns = [
    path('commandes', views.commandes, name='commandes'),
    path('ajouter_commande', views.ajouter_commande, name='ajouter_commande'),
    path('modifier_commande/(<id>[0-9]+)', views.modifier_commande, name='modifier_commande'),
    path('delete_commande/(<id>[0-9]+)', views.delete_commande, name='delete_commande'),
    path('affiche_commande/(<id>[0-9]+)', views.affiche_commande, name='affiche_commande'),

#
]
