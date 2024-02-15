from django.db import models
from gestionfournisseurs.models import Fournisseur

# Create your models here.


class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    libelle = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'categorie'

    def __str__(self):
        return self.libelle


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=50)
    quantite_stock = models.FloatField()
    prix_unitaire = models.FloatField()
    tva = models.FloatField()
    categorie = models.ForeignKey(Categorie, models.DO_NOTHING,null=True)
    fournisseur = models.ForeignKey(Fournisseur, models.DO_NOTHING,null=True)

    class Meta:
        managed = True
        db_table = 'article'
