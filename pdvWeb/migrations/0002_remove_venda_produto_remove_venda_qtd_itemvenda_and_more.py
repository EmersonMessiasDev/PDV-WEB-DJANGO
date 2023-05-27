# Generated by Django 4.2 on 2023-05-26 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pdvWeb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='venda',
            name='qtd',
        ),
        migrations.CreateModel(
            name='ItemVenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('subtotal', models.FloatField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdvWeb.produto')),
                ('venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdvWeb.venda')),
            ],
        ),
        migrations.AddField(
            model_name='venda',
            name='produtos',
            field=models.ManyToManyField(through='pdvWeb.ItemVenda', to='pdvWeb.produto'),
        ),
    ]