from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Personnel(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'personnel'
