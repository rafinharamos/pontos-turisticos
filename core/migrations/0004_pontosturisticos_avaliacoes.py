# Generated by Django 2.0.4 on 2018-11-29 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('core', '0003_pontosturisticos_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='avaliacoes',
            field=models.ManyToManyField(to='avaliacoes.Avaliacao'),
        ),
    ]