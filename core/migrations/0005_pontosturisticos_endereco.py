# Generated by Django 2.0.4 on 2018-11-29 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('core', '0004_pontosturisticos_avaliacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontosturisticos',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='enderecos.Enderecos'),
            preserve_default=False,
        ),
    ]
