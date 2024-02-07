from django.db import models

# Create your models here.


class Fournisseur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    num_compte = models.IntegerField()
    num_registre_commerce = models.IntegerField()

    def __str__(self):
        return self.nom + " " + self.prenom

    class Meta:
        managed = True
        db_table = 'fournisseur'