# Generated by Django 5.0.2 on 2024-03-09 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionpersonnels', '0003_auto_20200905_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnel',
            name='service',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
