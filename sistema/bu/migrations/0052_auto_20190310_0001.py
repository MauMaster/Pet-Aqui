# Generated by Django 2.1.7 on 2019-03-10 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0051_negocio_obs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='usuario_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
