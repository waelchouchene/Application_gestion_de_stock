# Generated by Django 5.0.2 on 2024-03-09 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionfournisseurs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fournisseur',
            name='fax',
            field=models.CharField(max_length=50, null=True),
        ),
    ]