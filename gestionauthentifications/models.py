from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=30)
    description = models.CharField(max_length=30, null=True, blank=True)
    code = models.IntegerField()

    class Meta:
        managed: True
        db_table = 'role'


class UserRole(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'userrole'
