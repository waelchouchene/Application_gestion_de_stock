from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from gestionauthentifications.models import UserRole, Role
from gestionpersonnels.models import Personnel, Service
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from gestioncommandes.models import Commande
# Create your views here.


@login_required(login_url='/gestionauthentifications/login')
def personnels(request):
    personnellist = Personnel.objects.all()
    servicelist=Service.objects.all()
    context = {'gestionPersonnelsMenu':'active','personnelsMenu':'active',
               'personnellist': personnellist,'servicelist':servicelist}
    return render(request, 'gestionpersonnels/personnels.html', context)


def ajouter_personnel(request):
    nom = request.POST['nom']
    prenom = request.POST['prenom']
    pseudo = request.POST['pseudo']
    password = request.POST['password']
    email = request.POST['email']
    idservice = request.POST['service']
    if request.POST.get("isadmin") == "checked":
        isadmin = True
    else:
        isadmin = False
    print(isadmin)
    service = Service.objects.get(pk=idservice)
    if(not User.objects.filter(username=pseudo)):
        user = User.objects.create_user(username=pseudo, password=password)
        print(user)
        p = Personnel(nom=nom,prenom=prenom,email=email,service=service,
                      user=user,
                      is_admin=isadmin)
        p.save()
    return HttpResponseRedirect(reverse('gestionpersonnels:personnels'))
#
#
def delete_personnel(request, id):
    p = Personnel.objects.get(pk=id)
    p.user.delete()
    p.delete()
    return HttpResponseRedirect(reverse('gestionpersonnels:personnels'))
#
#
def modifier_personnel(request, id):
    p = Personnel.objects.get(pk=id)
    personnellist = Personnel.objects.all()
    servicelist=Service.objects.all()
    context = {'personnelsMenu':'active','personnel':p,
               'personnellist':personnellist,'servicelist':servicelist}
    return render(request, 'gestionpersonnels/modifier_personnel.html', context)
#
def save_personnel(request, id):
    p = Personnel.objects.get(pk=id)
    user = p.user
    if request.method == "POST":
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        pseudo = request.POST['pseudo']
        email = request.POST['email']
        idservice = request.POST['service']
        service = Service.objects.get(pk=idservice)
        p.nom = nom
        p.prenom = prenom
        p.email = email
        p.service = service
        if request.POST.get("isadmin") == "checked":
            isadmin = True
        else:
            isadmin = False
        p.is_admin = isadmin
        user.username = pseudo
        p.save()
        user.save()
    return HttpResponseRedirect(reverse('gestionpersonnels:personnels'))


def change_password(request, id):
    personnel = Personnel.objects.get(pk=id)
    context = {"personnel": personnel, 'personnelsMenu':'active'}
    if request.method == "POST":
        old_password = request.POST['oldPassword']
        new_password = request.POST['newPassword']
        confirm_new_password = request.POST['confirmNewPassword']
        error_message = ""
        success_message = ""
        if old_password and new_password and confirm_new_password:
            user = authenticate(username=personnel.user.username, password=old_password)
            if user:
                if new_password == confirm_new_password:
                    personnel.user.set_password(new_password)
                    personnel.user.save()
                    success_message = "Mot de passe changé avec succès"
                else:
                    error_message = "Faut confirmer avec le même mot de passe"
            else:
                error_message = "Mot de passe incorrect"
        else:
            error_message = "Il faut remplir tous les champs"
        context.update({"error_message": error_message, "success_message": success_message})
    return render(request, 'gestionpersonnels/change_password.html', context)


def affiche_commande_personnel(request,id):
    commandelist = Commande.objects.filter(personnel__id=id)
    context={"commandelist": commandelist, 'commandesMenu': 'active'}
    return render(request,'gestioncommandes/commandes.html', context)
