# Generated by Django 2.1.7 on 2019-02-24 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0040_usuario_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='about',
            field=models.CharField(blank=True, max_length=600, verbose_name='Sobre você'),
        ),
    ]
