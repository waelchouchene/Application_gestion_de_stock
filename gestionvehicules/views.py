from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db import models
from django.contrib.auth.decorators import login_required
from gestionlivraisons.models import Livraison
from gestionvehicules.models import Vehicule
from gestionpersonnels.models import Personnel

# Create your views here.
# from generic_app.models import Agence, Assure

@login_required(login_url='/gestionauthentifications/login')
def vehicules(request):

    vehiculelist = Vehicule.objects.all()
    personnellist = Personnel.objects.all()
    context = {'vehiculesmenu':'active', 'vehiculelist':vehiculelist,'personnellist':personnellist}
    return render(request, 'gestionvehicules/vehicules.html', context)

def ajouter_vehicule(request):
    matricule = request.POST['matricule']
    type = request.POST['type']
    idchauffeur=request.POST['chauffeur']
    chauffeur=Personnel.objects.get(pk=idchauffeur)
    vehiculelist=Vehicule.objects.all()
    if (Vehicule.objects.filter(matricule=matricule).exists()):
        error_message = "Véhicule existe déja"
        return render(request,'gestionvehicules/vehicules.html',{'error_message':error_message,'vehiculelist':vehiculelist})
    else:
        v = Vehicule (matricule=matricule,type=type,chauffeur=chauffeur)
        v.save()
    return HttpResponseRedirect(reverse('gestionvehicules:vehicules'))

def modifier_vehicule(request, id):
    v = Vehicule.objects.get(pk=id)
    personnellist = Personnel.objects.all()
    vehiculelist = Vehicule.objects.all()
    return render(request, 'gestionvehicules/modifier_vehicule.html', {'vehiculesMenu':'active', 'vehicule':v, 'vehiculelist':vehiculelist,'personnellist':personnellist})

def delete_vehicule(request, id):
    v = Vehicule.objects.get(pk=id)
    v.delete()
    return HttpResponseRedirect(reverse('gestionvehicules:vehicules'))

def save_vehicule(request, id):
    v = Vehicule.objects.get(pk=id)
    if request.method == "POST":
        matricule = request.POST['matricule']
        type = request.POST['type']
        #chauffeur = request.POST['chauffeur']
        idchauffeur=request.POST['chauffeur']
        chauffeur=Personnel.objects.get(pk=idchauffeur)
        v.matricule = matricule
        v.type = type
        v.chauffeur = chauffeur
        v.save()
    return HttpResponseRedirect(reverse('gestionvehicules:vehicules'))
