from django.urls import path

from . import views

app_name = 'gestionlivraisons'
urlpatterns = [
    path('livraisons', views.livraisons, name='livraisons'),
    path('ajouter_livraison', views.ajouter_livraison, name='ajouter_livraison'),
    path('modifier_livraison/(<id>[0-9]+)', views.modifier_livraison, name='modifier_livraison'),
    path('save_livraison/(<id>[0-9]+)', views.save_livraison, name='save_livraison'),
    path('delete_livraison/(<id>[0-9]+)', views.delete_livraison, name='delete_livraison'),
    path('generate_pdf/(<livraison_id>[0-9]+)', views.generate_livraison, name='generate_livraison'),
    path('affiche_livraison/(<id>[0-9]+)', views.affiche_livraison, name='affiche_livraison'),
    path('generate_pdf/(<livraison_id>[0-9]+)', views.generate_livraison, name='generate_livraison'),

]
