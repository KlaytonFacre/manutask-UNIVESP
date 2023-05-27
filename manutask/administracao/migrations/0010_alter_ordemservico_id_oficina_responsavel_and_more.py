# Generated by Django 4.2.1 on 2023-05-25 00:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0009_alter_ordemservico_timestamp_abertura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemservico',
            name='id_oficina_responsavel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administracao.oficina'),
        ),
        migrations.AlterField(
            model_name='ordemservico',
            name='id_solucionador',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='solucionador', to='administracao.pessoa'),
        ),
        migrations.AlterField(
            model_name='ordemservico',
            name='timestamp_abertura',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 24, 21, 30, 16, 232254)),
        ),
    ]
