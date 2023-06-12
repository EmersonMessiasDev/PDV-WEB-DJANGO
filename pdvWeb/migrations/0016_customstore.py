# Generated by Django 4.2 on 2023-06-11 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdvWeb', '0015_alter_venda_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('logoImage', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
