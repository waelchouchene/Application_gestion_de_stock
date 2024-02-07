from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from gestionarticles.models import Article
from gestionclients.models import Client
from gestioncommandes.models import Commande
from gestionpersonnels.models import Personnel
from .services import commandeService
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/gestionauthentifications/login')
def commandes(request):
    commandelist = Commande.objects.all()
    context = {'commandesMenu': 'active', 'commandelist': commandelist}
    return render(request, 'gestioncommandes/commandes.html',context)


@login_required(login_url='/gestionauthentifications/login')
def ajouter_commande(request):
    clientlist = Client.objects.all()
    personnellist = Personnel.objects.all()
    articlelist = Article.objects.filter(quantite_stock__gte=1)
    context = {'commandesMenu': 'active','clientlist': clientlist,
               'personnellist': personnellist, 'articlelist': articlelist}
    if(request.method == "POST"):
        commande = commandeService.save_commande(request)
        return HttpResponseRedirect(reverse('gestioncommandes:affiche_commande', args=[commande.id]))
    return render(request, 'gestioncommandes/ajouter_commande.html', context)


@login_required(login_url='/gestionauthentifications/login')
def modifier_commande(request, id):
    c = Commande.objects.get(pk=id)
    clientlist = Client.objects.all()
    articlelist = Article.objects.all()
    personnellist = Personnel.objects.all()
    context = {'commandesMenu': 'active', 'articlelist': articlelist,
               'clientlist': clientlist, 'personnellist': personnellist,
               'commande': c}
    if(request.method == "POST"):
        commande = commandeService.save_commande(request, c.id)
        return HttpResponseRedirect(reverse('gestioncommandes:affiche_commande', args=[commande.id]))
    return render(request, 'gestioncommandes/modifier_commande.html', context)


def affiche_commande(request,id):
    commande = Commande.objects.get(pk=id)
    context = {'commandesMenu': 'active', 'commande': commande}
    return render(request, 'gestioncommandes/affiche_commande.html', context)
    return render(request, 'gestioncommandes/affiche_commande.html', context)


def delete_commande(request, id):
    c = Commande.objects.get(pk=id)
    for dc in c.detailscommande_set.all():
        dc.delete()
    c.delete()
    return HttpResponseRedirect(reverse('gestioncommandes:commandes'))
