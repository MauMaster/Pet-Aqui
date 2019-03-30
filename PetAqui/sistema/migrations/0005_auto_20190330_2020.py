# Generated by Django 2.1.7 on 2019-03-30 20:20

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0004_auto_20190330_2019'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PetAceitos',
        ),
        migrations.AlterField(
            model_name='negocio',
            name='pet_aceitos',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Cachorro Pequeno Porte', 'Cachorro Pequeno Porte'), ('Cachorro Médio Porte', 'Cachorro Médio Porte'), ('Cachorro Grande Porte', 'Cachorro Grande Porte'), ('Gato', 'Gato'), ('Pássaros', 'Pássaros'), ('Peixes', 'Peixes'), ('Reptéis', 'Reptéis'), ('Roedores', 'Roedores')], max_length=255),
        ),
    ]
