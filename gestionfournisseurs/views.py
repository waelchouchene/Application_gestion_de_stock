from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Fournisseur
from django.contrib.auth.decorators import login_required

# Create your views here.
# from generic_app.models import Agence, Assure


@login_required(login_url='/gestionauthentifications/login')
def fournisseurs(request):
    fournisseurlist = Fournisseur.objects.all()
    return render(request, 'gestionfournisseurs/fournisseurs.html', {'fournisseursMenu':'active','fournisseurlist':fournisseurlist})


def ajouter_fournisseur(request):
    nom = request.POST['nom']
    prenom = request.POST['prenom']
    adresse = request.POST['adresse']
    telephone = request.POST['telephone']
    email = request.POST['email']
    numcompte = request.POST['numcompte']
    numregistrecommerce = request.POST['numregistrecommerce']
    f = Fournisseur(nom=nom,
                    prenom=prenom,
                    adresse=adresse,
                    telephone=telephone,
                    email=email,
                    num_compte=numcompte,
                    num_registre_commerce=numregistrecommerce)
    f.save()
    return HttpResponseRedirect(reverse('gestionfournisseurs:fournisseurs'))


def delete_fournisseur(request, id):
    f = Fournisseur.objects.get(pk=id)
    f.delete()
    return HttpResponseRedirect(reverse('gestionfournisseurs:fournisseurs'))


def modifier_fournisseur(request, id):
    f = Fournisseur.objects.get(pk=id)
    print ('******',f.nom)
    fournisseurlist = Fournisseur.objects.all()
    return render(request, 'gestionfournisseurs/modifier_fournisseur.html', {'fournisseursMenu':'active','fournisseurlist':fournisseurlist,'fournisseur':f})


def save_fournisseur(request, id):
    f = Fournisseur.objects.get(pk=id)
    if request.method == "POST":
        nom = request.POST['nom']
        print ('Nom = ',nom)
        prenom = request.POST['prenom']
        print('Prénom = ',prenom)
        adresse = request.POST['adresse']
        telephone = request.POST['telephone']
        email = request.POST['email']
        numcompte = request.POST['numcompte']
        numregistrecommerce = request.POST['numregistrecommerce']
        f.nom = nom
        f.nom = prenom
        f.adresse = adresse
        f.telephone = telephone
        f.email = email
        f.num_compte = numcompte
        f.num_registre_commerce = numregistrecommerce
        f.save()
    return HttpResponseRedirect(reverse('gestionfournisseurs:fournisseurs'))
