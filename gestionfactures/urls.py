from django.urls import path

from . import views

app_name = 'gestionfactures'
urlpatterns = [
       path('some_view', views.some_view, name='some_view'),
       path('generate_pdf/(<commande_id>[0-9]+)', views.generate_facture, name='generate_facture'),
    ]
