# Generated by Django 2.1.7 on 2019-03-15 12:50

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0057_remove_negocio_senha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='negocio',
            name='horario',
        ),
        migrations.RemoveField(
            model_name='negocio',
            name='nome',
        ),
        migrations.AddField(
            model_name='negocio',
            name='empresa',
            field=models.CharField(default=2, max_length=50, verbose_name='Nome da Empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='negocio',
            name='horario_segunda1',
            field=models.TimeField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='negocio',
            name='horario_segunda2',
            field=models.TimeField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='negocio',
            name='horario_segunda3',
            field=models.TimeField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='negocio',
            name='horario_segunda4',
            field=models.TimeField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='negocio',
            name='segunda',
            field=models.CharField(default='Segunda', max_length=50),
        ),
        migrations.AddField(
            model_name='negocio',
            name='whatsapp',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='negocio',
            name='pet_aceitos',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('PDog', 'Cachorro Pequeno Porte'), ('MDog', 'Cachorro Médio Porte'), ('GDog', 'Cachorro Grande Porte'), ('cat', 'Gato'), ('bird', 'Pássaros'), ('fish', 'Peixes'), ('rep', 'Reptéis'), ('rat', 'Roedores')], default='dog', max_length=2),
        ),
        migrations.AlterField(
            model_name='negocio',
            name='tipo',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('H', 'Hotéis'), ('PS', 'PetShops'), ('V', 'Veterinários'), ('R', 'Restaurantes'), ('C', 'Cafés'), ('HP', 'HotéisPet')], max_length=100, verbose_name='Tipo de negocio'),
        ),
    ]
