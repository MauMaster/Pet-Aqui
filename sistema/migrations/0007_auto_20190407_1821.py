# Generated by Django 2.1.7 on 2019-04-07 18:21

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0006_usuario_galerry_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='galerry_usuario',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to=''),
        ),
    ]
