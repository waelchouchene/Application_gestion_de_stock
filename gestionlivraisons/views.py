from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db import models
from django.contrib.auth.decorators import login_required
from gestionlivraisons.models import Livraison
from gestionvehicules.models import Vehicule
from gestioncommandes.models import Commande
from gestionpersonnels.models import Personnel
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
import xhtml2pdf.pisa as pisa
from django.template.loader import get_template
from django.http import HttpResponse
from gestionlivraisons.models import Livraison
from datetime import datetime

# Create your views here.


@login_required(login_url='/gestionauthentifications/login')

def livraisons(request):

    livraisonlist = Livraison.objects.all()
    vehiculelist = Vehicule.objects.all()
    commandelist = Commande.objects.all()
    personnellist = Personnel.objects.all()
    context = {'livraisonsMenu':'active','livraisonlist':livraisonlist,'vehiculelist':vehiculelist,
               'commandelist':commandelist,'personnellist':personnellist}
    return render(request, 'gestionlivraisons/livraisons.html', context)

def ajouter_livraison(request):
    date = request.POST['date']
    idcommande=request.POST['commande']
    commande=Commande.objects.get(pk=idcommande)
    idvehicule=request.POST['vehicule']
    vehicule=Vehicule.objects.get(pk=idvehicule)
    idchauffeur=request.POST['chauffeur']
    chauffeur=Personnel.objects.get(pk=idchauffeur)
    l = Livraison(date=date,commande=commande,vehicule=vehicule,chauffeur=chauffeur)
    l.save()
    return HttpResponseRedirect(reverse('gestionlivraisons:livraisons'))

def save_livraison(request, id):
    l = Livraison.objects.get(pk=id)
    if request.method == "POST":
        date = request.POST['date']
        idcommande=request.POST['commande']
        commande=Commande.objects.get(pk=idcommande)
        idvehicule=request.POST['vehicule']
        vehicule=Vehicule.objects.get(pk=idvehicule)
        idchauffeur=request.POST['chauffeur']
        chauffeur=Personnel.objects.get(pk=idchauffeur)
        l.date = date
        l.commande = commande
        l.vehicule = vehicule
        l.chauffeur = chauffeur
        print("avant")
        l.save()
        print("apres")
    return HttpResponseRedirect(reverse('gestionlivraisons:livraisons'))

def modifier_livraison(request, id):
    l = Livraison.objects.get(pk=id)
    livraisonlist = Livraison.objects.all()
    vehiculelist = Vehicule.objects.all()
    commandelist=Commande.objects.all()
    personnellist=Personnel.objects.all()
    return render(request, 'gestionlivraisons/modifier_livraison.html', {'livraisonsMenu':'active', 'livraison':l,
                                                                         'livraisonlist':livraisonlist,'vehiculelist':vehiculelist,
                                                                         'commandelist': commandelist,'personnellist': personnellist})
def affiche_livraison(request, id):
    livraison = Livraison.objects.get(pk=id)
    context = {'livraisonsMenu': 'active', 'livraison': livraison}
    return render(request, 'gestionlivraisons/affiche_livraison.html', context)


def delete_livraison(request, id):
    l = Livraison.objects.get(pk=id)
    l.delete()
    return HttpResponseRedirect(reverse('gestionlivraisons:livraisons'))

def generate_livraison(request, livraison_id):
    livraison = Livraison.objects.get(pk=livraison_id)
    params = {"livraison": livraison, "dateNow": datetime.now()}
    template = get_template("gestionlivraisons/pdf.html")
    html = template.render(params)
    response = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), response)
    response.seek(0)
    if not pdf.err:
        return FileResponse(response, as_attachment=True, filename='livraison'+str(livraison.id)+str(livraison.commande.libelle)+'.pdf')
    else:
        return HttpResponse("Error Rendering PDF", status=400)
