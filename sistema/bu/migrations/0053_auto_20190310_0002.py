# Generated by Django 2.1.7 on 2019-03-10 00:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0052_auto_20190310_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='usuario_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
