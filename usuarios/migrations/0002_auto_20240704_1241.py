# Generated by Django 2.2.5 on 2024-07-04 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelusuario',
            name='fone',
            field=models.CharField(max_length=15, verbose_name='fone'),
        ),
        migrations.AlterField(
            model_name='modelusuario',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Staff Member'),
        ),
    ]