# Generated by Django 4.2 on 2023-06-09 04:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdvWeb', '0003_rename_nome_produto_descricao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]