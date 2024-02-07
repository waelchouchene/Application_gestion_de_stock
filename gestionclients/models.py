from django.db import models

# Create your models here.


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    adresse = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'client'

    def __str__(self):
        return self.prenom + " " + self.nom