# Generated by Django 2.1.5 on 2019-01-09 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0016_auto_20190108_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(upload_to='foto'),
        ),
    ]
