# Generated by Django 3.0.7 on 2020-09-05 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpersonnels', '0002_auto_20200905_2030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personnel',
            old_name='id_admin',
            new_name='is_admin',
        ),
    ]
