from django.urls import path

from . import views

app_name = 'gestionlivraisons'
urlpatterns = [
    path('livraisons', views.livraisons, name='livraisons'),
    path('ajouter_livraison', views.ajouter_livraison, name='ajouter_livraison'),
    path('modifier_livraison/(<id>[0-9]+)', views.modifier_livraison, name='modifier_livraison'),
    path('save_livraison/(<id>[0-9]+)', views.save_livraison, name='save_livraison'),
    path('delete_livraison/(<id>[0-9]+)', views.delete_livraison, name='delete_livraison'),

]
