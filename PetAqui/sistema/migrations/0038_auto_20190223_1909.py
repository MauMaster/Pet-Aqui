# Generated by Django 2.1.7 on 2019-02-23 19:09

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0037_auto_20190219_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=stdimage.models.StdImageField(default='static/img/24.jpg', upload_to=''),
        ),
    ]
