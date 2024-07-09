# Generated by Django 2.2.5 on 2024-07-09 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20240708_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='compra_url',
            field=models.CharField(default='#', max_length=200, verbose_name='Link compra'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='imagem_url',
            field=models.CharField(default='#', max_length=200, verbose_name='URL IMG'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='preco',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=10, verbose_name='Preço'),
        ),
    ]
