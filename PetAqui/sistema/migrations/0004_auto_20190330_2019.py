# Generated by Django 2.1.7 on 2019-03-30 20:19

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_auto_20190330_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petaceitos',
            name='pet_aceitos',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Cachorro Pequeno Porte', 'Cachorro Pequeno Porte'), ('Cachorro Médio Porte', 'Cachorro Médio Porte'), ('Cachorro Grande Porte', 'Cachorro Grande Porte'), ('Gato', 'Gato'), ('Pássaros', 'Pássaros'), ('Peixes', 'Peixes'), ('Reptéis', 'Reptéis'), ('Roedores', 'Roedores')], max_length=255),
        ),
    ]