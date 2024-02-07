from django.db import models
from gestioncommandes.models import Commande,Personnel
from gestionvehicules.models import Vehicule


# Create your models here.


class Livraison(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    montant_total = models.FloatField()
    commande = models.ForeignKey(Commande, models.DO_NOTHING)
    vehicule = models.ForeignKey(Vehicule, models.DO_NOTHING)

    def __str__(self):
            return self.commande.libelle
    class Meta:
        managed = True
        db_table = 'livraison'

