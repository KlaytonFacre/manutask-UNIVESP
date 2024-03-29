# Generated by Django 4.2.1 on 2023-05-27 17:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0012_alter_ordemservico_timestamp_abertura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemservico',
            name='id_solucionador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solucionador', to='administracao.pessoa'),
        ),
        migrations.AlterField(
            model_name='ordemservico',
            name='timestamp_abertura',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 27, 14, 21, 11, 997332)),
        ),
    ]
