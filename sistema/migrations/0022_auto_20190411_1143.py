# Generated by Django 2.1.7 on 2019-04-11 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0021_auto_20190411_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.FileField(upload_to='photos/'),
        ),
    ]
