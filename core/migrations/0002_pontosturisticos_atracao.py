# Generated by Django 2.0.1 on 2018-11-21 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracoes', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='atracao',
            field=models.ManyToManyField(to='atracoes.Atracao'),
        ),
    ]
