# Generated by Django 4.2 on 2023-06-09 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdvWeb', '0004_venda_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='cpf_cliente',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
