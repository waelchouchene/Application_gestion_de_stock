from django.urls import path

from . import views

app_name = 'gestionvehicules'
urlpatterns = [
    path('vehicules', views.vehicules, name='vehicules'),
    path('ajouter_vehicule', views.ajouter_vehicule, name='ajouter_vehicule'),
    path('modifier_vehicule/(<id>[0-9]+)', views.modifier_vehicule, name='modifier_vehicule'),
    path('save_vehicule/(<id>[0-9]+)', views.save_vehicule, name='save_vehicule'),
    path('delete_vehicule/(<id>[0-9]+)', views.delete_vehicule, name='delete_vehicule'),

]
