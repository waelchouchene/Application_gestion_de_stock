from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    intitule = models.CharField(max_length=30)
    nom_responsable = models.CharField(max_length=20)
    prenom_responsable = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'service'


class Personnel(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    service = models.ForeignKey(Service, models.DO_NOTHING)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'personnel'
    def __str__(self):
        return self.nom +' '+self.prenom
