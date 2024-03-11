from django.db import models
from gestionfournisseurs.models import Fournisseur

# Create your models here.


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=50)
    quantite_stock = models.FloatField()
    prix_unitaire = models.FloatField()
    tva = models.FloatField()
    fournisseur = models.ForeignKey(Fournisseur, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'article'