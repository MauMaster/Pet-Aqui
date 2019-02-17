# Generated by Django 2.1.5 on 2019-01-27 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0008_auto_20190127_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='email_confirmed',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='user',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(max_length=19, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
