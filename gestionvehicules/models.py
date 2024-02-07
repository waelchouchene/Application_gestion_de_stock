from django.db import models
from gestionpersonnels.models import Personnel

# Create your models here.
class Vehicule(models.Model):
    id = models.AutoField(primary_key=True)
    matricule = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    chauffeur = models.ForeignKey(Personnel, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'vehicule'

    def __str__(self):
        return self.matricule
