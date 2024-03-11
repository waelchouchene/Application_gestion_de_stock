from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from gestionarticles.models import Article
from gestionfournisseurs.models import Fournisseur
from gestioncommandes.models import Commande
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/gestionauthentifications/login')

def articles(request):
    articlelist = Article.objects.all()
    fournisseurlist = Fournisseur.objects.all()
    return render(request, 'gestionarticles/articles.html', {'articlesMenu':'active','articlelist':articlelist,
                                                             'fournisseurlist':fournisseurlist})
#
#
def ajouter_article(request):
    articlelist = Article.objects.all()
    designation = request.POST['designation']
    quantitestock = request.POST['quantitestock']
    prixunitaire = request.POST['prixunitaire']
    tva = request.POST['tva']
    newtva = tva
    idfournisseur=request.POST['fournisseur']
    fournisseur=Fournisseur.objects.get(pk=idfournisseur)
    if(Article.objects.filter(designation=designation).exists()):
        error_message = "Article existe déja"
        return render(request,'gestionarticles/articles.html',{'error_message':error_message,'articlelist':articlelist})
    else:
        a = Article(designation=designation,quantite_stock=quantitestock,
                    prix_unitaire=prixunitaire,tva=newtva,fournisseur=fournisseur)
        a.save()
    return HttpResponseRedirect(reverse('gestionarticles:articles'))
#
#
def delete_article(request, id):
    a = Article.objects.get(pk=id)
    print('avant********')
    a.delete()
    print('après********')
    return HttpResponseRedirect(reverse('gestionarticles:articles'))
#
#
def modifier_article(request, id):
    a = Article.objects.get(pk=id)
    articlelist = Article.objects.all()
    fournisseurlist=Fournisseur.objects.all()
    context = {'articlesMenu':'active','article':a,
               'fournisseurlist':fournisseurlist,
               'articlelist':articlelist}
    return render(request, 'gestionarticles/modifier_article.html', context)
#
#
def save_article(request, id):
    a = Article.objects.get(pk=id)
    if request.method == "POST":
        designation = request.POST['designation']
        quantitestock = request.POST['quantitestock']
        prixunitaire = request.POST['prixunitaire']
        tva = request.POST['tva']
        newtva = tva
        idfournisseur = request.POST['fournisseur']
        fournisseur = Fournisseur.objects.get(pk=idfournisseur)
        a.designation = designation
        a.quantite_stock = quantitestock
        a.prix_unitaire = prixunitaire
        a.tva = newtva
        a.fournisseur = fournisseur
        a.save()
    return HttpResponseRedirect(reverse('gestionarticles:articles'))


def affiche_commande_article(request, id):
    commandelist = Commande.objects.filter(detailscommande__article__id=id)
    context = {'commandelist': commandelist, 'commandesMenu': 'active'}
    return render(request, 'gestioncommandes/commandes.html', context)
