# Generated by Django 2.1.5 on 2019-01-28 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0011_remove_usuario_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='negocio',
            name='estado',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='negocio',
            name='pet_aceitos',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='estado',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pet',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(max_length=2),
        ),
    ]
