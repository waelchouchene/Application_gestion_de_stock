from django.urls import path

from . import views

app_name = 'gestionarticles'
urlpatterns = [
    path('articles', views.articles, name='articles'),
    path('ajouter_article', views.ajouter_article, name='ajouter_article'),
    path('modifier_article/(<id>[0-9]+)', views.modifier_article, name='modifier_article'),
    path('save_article/(<id>[0-9]+)', views.save_article, name='save_article'),
    path('delete_article/(<id>[0-9]+)', views.delete_article, name='delete_article'),
    path('affiche_commande_article/(<id>[0-9]+)', views.affiche_commande_article, name='affiche_commande_article'),
]
