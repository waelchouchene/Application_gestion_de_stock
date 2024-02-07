from django.urls import path

from . import views

app_name = 'gestionpersonnels'
urlpatterns = [
    path('personnels', views.personnels, name='personnels'),
    path('ajouter_personnel', views.ajouter_personnel, name='ajouter_personnel'),
    path('modifier_personnel/(<id>[0-9]+)', views.modifier_personnel, name='modifier_personnel'),
    path('save_personnel/(<id>[0-9]+)', views.save_personnel, name='save_personnel'),
    path('delete_personnel/(<id>[0-9]+)', views.delete_personnel, name='delete_personnel'),
    path('change_password/(<id>[0-9]+)', views.change_password, name='change_password'),
    path('affiche_commande_personnel/(<id>[0-9]+)', views.affiche_commande_personnel, name='affiche_commande_personnel'),

]
