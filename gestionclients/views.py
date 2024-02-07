from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db import models
from gestionclients.models import Client
from gestioncommandes.models import Commande
from django.contrib.auth.decorators import login_required

# Create your views here.
# from generic_app.models import Agence, Assure

@login_required(login_url='/gestionauthentifications/login')
def clients(request):

    clientlist = Client.objects.all()
    context = {'clientsMenu':'active', 'clientlist':clientlist}
    return render(request, 'gestionclients/clients.html', context)

#
def ajouter_client(request):
    nomclient = request.POST['nom']
    prenomclient = request.POST['prenom']
    adresseclient = request.POST['adresse']
    emailclient = request.POST['email']
    telephoneclient = request.POST['telephone']
    clientlist=Client.objects.all()
    if (Client.objects.filter(email=emailclient).exists()):
        error_message = "Client existe déja"
        return render(request,'gestionclients/clients.html',{'error_message':error_message,'clientlist':clientlist})
    else:
        c = Client (nom=nomclient,prenom=prenomclient,adresse=adresseclient,email=emailclient,telephone=telephoneclient)
        c.save()
    return HttpResponseRedirect(reverse('gestionclients:clients'))

def modifier_client(request, id):
    c = Client.objects.get(pk=id)
    clientlist = Client.objects.all()
    return render(request, 'gestionclients/modifier_client.html', {'clientsMenu':'active', 'client':c, 'clientlist':clientlist})

def delete_client(request, id):
    c = Client.objects.get(pk=id)
    c.delete()
    return HttpResponseRedirect(reverse('gestionclients:clients'))

def save_client(request, id):
    c = Client.objects.get(pk=id)
    if request.method == "POST":
        nomclient = request.POST['nom']
        prenomclient = request.POST['prenom']
        adresseclient = request.POST['adresse']
        emailclient = request.POST['email']
        telephoneclient= request.POST['telephone']
        c.nom = nomclient
        c.prenom = prenomclient
        c.adresse = adresseclient
        c.email = emailclient
        c.telephone = telephoneclient
        c.save()
    return HttpResponseRedirect(reverse('gestionclients:clients'))


def affiche_commande_client (request, id):
    commandelist = Commande.objects.filter(client__id=id)
    context = {'commandelist':commandelist}
    return render(request, 'gestioncommandes/commandes.html',context)
