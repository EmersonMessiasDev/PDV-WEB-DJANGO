# Generated by Django 4.2 on 2023-06-09 17:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdvWeb', '0010_alter_venda_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 9, 17, 51, 34, 827273, tzinfo=datetime.timezone.utc)),
        ),
    ]