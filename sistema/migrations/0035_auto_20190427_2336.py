# Generated by Django 2.1.7 on 2019-04-27 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0034_comentario_nome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='nome',
            new_name='nome2',
        ),
    ]