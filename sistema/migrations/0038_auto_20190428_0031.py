# Generated by Django 2.1.7 on 2019-04-28 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0037_comentario_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='nome',
        ),
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
