from django.db import models
from gestionarticles.models import Article
from gestionclients.models import Client
from gestionpersonnels.models import Personnel

# Create your models here.


class Commande(models.Model):
    id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=50)
    date = models.DateField()
    client = models.ForeignKey(Client, models.DO_NOTHING,null=True)
    personnel = models.ForeignKey(Personnel, models.DO_NOTHING, null=True)
    total_prix_ht = models.FloatField()
    total_prix_ttc = models.FloatField()

    class Meta:
        managed = True
        db_table = 'commande'

    def __str__(self):
        return 'Commande '+ str(self.id)

class DetailsCommande(models.Model):
    id = models.AutoField(primary_key=True)
    commande = models.ForeignKey(Commande, models.DO_NOTHING,null=True)
    article = models.ForeignKey(Article, models.DO_NOTHING,null=True)
    qtecommande = models.IntegerField()
    prix_ht = models.FloatField()
    prix_ttc = models.FloatField()

    class Meta:
        managed = True
        db_table = 'detailscommande'
