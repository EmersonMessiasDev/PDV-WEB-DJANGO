# Generated by Django 4.2 on 2023-06-09 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdvWeb', '0011_alter_venda_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateTimeField(),
        ),
    ]
