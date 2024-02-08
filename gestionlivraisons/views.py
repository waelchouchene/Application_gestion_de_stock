from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db import models
from django.contrib.auth.decorators import login_required
from gestionlivraisons.models import Livraison
from gestionvehicules.models import Vehicule
from gestioncommandes.models import Commande
from gestionpersonnels.models import Personnel


# Create your views here.


@login_required(login_url='/gestionauthentifications/login')

def livraisons(request):

    livraisonlist = Livraison.objects.all()
    vehiculelist = Vehicule.objects.all()
    commandelist = Commande.objects.all()
    personnellist = Personnel.objects.all()
    context = {'livraisonsMenu':'active','livraisontlist':livraisonlist,'vehiculelist':vehiculelist,
               'commandelist':commandelist,'personnellist':personnellist}
    return render(request, 'gestionlivraisons/livraisons.html', context)

def ajouter_livraison(request):
    date = request.POST['date']
    montant_total = request.POST['montant_total']
    # commande = request.POST['commande']
    idcommande=request.POST['commande']
    commande=Commande.objects.get(pk=idcommande)
    #vehicule = request.POST['vehicule']
    idcvehicule=request.POST['vehicule']
    vehicule=Vehicule.objects.get(pk=idcvehicule)
    l = Livraison(date=date,montant_total=montant_total,commande=commande,vehicule=vehicule)
    l.save()
    return HttpResponseRedirect(reverse('gestionlivraisons:livraisons'))

def save_livraison(request, id):
    l = Livraison.objects.get(pk=id)
    if request.method == "POST":
        date = request.POST['date']
        montant_total = request.POST['montant_total']
        commande = request.POST['commande']
        #vehicule = request.POST['vehicule']
        idcvehicule=request.POST['vehicule']
        vehicule=Vehicule.objects.get(pk=idcvehicule)
        l.date = date
        l.montant_total = montant_total
        l.commande = commande
        l.vehicule = vehicule
        l.save()
    return HttpResponseRedirect(reverse('gestionlivraisons:livraisons'))

def modifier_livraison(request, id):
    l = Livraison.objects.get(pk=id)
    livraisontlist = Livraison.objects.all()
    vehiculetlist = Vehicule.objects.all()
    commandelist=Commande.objects.all()
    return render(request, 'gestionlivraisons/modifier_livraison.html', {'livraisonsMenu':'active', 'livraison':l,
                                                                         'livraisontlist':livraisontlist,'vehiculetlist':vehiculetlist,
                                                                         'commandelist':commandelist,'personnellist':personnellist})

def delete_livraison(request, id):
    l = Livraison.objects.get(pk=id)
    l.delete()
    return HttpResponseRedirect(reverse('gestionlivraisons:livraisons'))
