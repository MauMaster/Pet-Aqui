# Generated by Django 2.1.7 on 2019-04-28 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0036_remove_comentario_nome2'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='nome',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='sistema.Usuario'),
            preserve_default=False,
        ),
    ]
