import datetime
from gestionclients.models import Client
from gestioncommandes.models import Commande, DetailsCommande
from gestionpersonnels.models import Personnel
from gestionarticles.models import Article


def save_commande(request, commande_id=None):
    post = request.POST
    libelle = post['libelle']
    date = datetime.datetime.strptime(post['date'], '%d-%m-%Y').strftime('%Y-%m-%d')
    idclient = post['client']
    client = Client.objects.get(pk=idclient)
    personnel = None
    try:
       personnel = request.user.personnel
    except Exception as e:
        pass
    if commande_id:
        commande = Commande.objects.get(pk=commande_id)
        commande.libelle = libelle
        commande.date = date
        commande.client = client
        commande.personnel = personnel
    else:
        commande = Commande.objects.create(libelle=libelle, date=date,
                                        client=client, personnel=personnel,
                                        total_prix_ht=0, total_prix_ttc=0)
    commande.save()
    existingCommandeDetails = {}
    submittedCommandeDetails = {}
    for cd in commande.detailscommande_set.all():
        existingCommandeDetails.update({cd.article.id: cd.qtecommande})
    for key, value in post.items():
        if (key.startswith('article_')):
            value = int(value)
            qt = int(post['quantite_'+key.split('_')[1]])
            print(key, value, qt)
            if(value in submittedCommandeDetails.keys()):
                print("update")
                submittedCommandeDetails[value] = submittedCommandeDetails[value]+qt
            else:
                print("ajout")
                submittedCommandeDetails.update({value: qt})
    print("existingCommandeDetails")
    print(existingCommandeDetails)
    print("submittedCommandeDetails")
    print(submittedCommandeDetails)
    commandeDetailsToDelete = []
    commandeDetailsToUpdate = {}
    commandeDetailsToAdd = {}
    for key, value in submittedCommandeDetails.items():
        if value == 0:
            if key in existingCommandeDetails.keys():
                commandeDetailsToDelete.append(key)
        else:
            if key not in existingCommandeDetails.keys():
                commandeDetailsToAdd.update({key: value})
            else:
                commandeDetailsToUpdate.update({key: value})
    print("commandeDetailsToDelete")
    print(commandeDetailsToDelete)
    print("commandeDetailsToAdd")
    print(commandeDetailsToAdd)
    print("commandeDetailsToUpdate")
    print(commandeDetailsToUpdate)
    for cdId in commandeDetailsToDelete:
        cdd = DetailsCommande.objects.filter(commande=commande, article_id=cdId)[0]
        cdd.delete()
    for key, value in commandeDetailsToUpdate.items():
        article = Article.objects.get(pk=key)
        cdd = DetailsCommande.objects.filter(commande=commande, article=article)[0]
        cdd.qtecommande = value
        cdd.prix_ht, cdd.prix_ttc = calculate_ht_ttc(article, value)
        cdd.save()
    for key, value in commandeDetailsToAdd.items():
        article = Article.objects.get(pk=key)
        cdd = DetailsCommande(commande=commande, article=article, qtecommande=value,
                              prix_ht=0, prix_ttc=0)
        cdd.prix_ht, cdd.prix_ttc = calculate_ht_ttc(article, value)
        cdd.save()
    updateCommadeHtTtc(commande)
    return commande


def calculate_ht_ttc(article, qt):
    ht = article.prix_unitaire*float(qt)
    ttc = ht+ht*article.tva/100
    return ht, ttc


def updateCommadeHtTtc(commande):
    total_price_ht = 0
    total_price_ttc = 0
    for cd in commande.detailscommande_set.all():
        total_price_ht += cd.prix_ht
        total_price_ttc += cd.prix_ttc
    commande.total_prix_ht = total_price_ht
    commande.total_prix_ttc = total_price_ttc
    commande.save()