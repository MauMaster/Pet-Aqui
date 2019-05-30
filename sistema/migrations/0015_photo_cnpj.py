# Generated by Django 2.1.7 on 2019-04-10 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0014_remove_photo_cnpj'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='cnpj',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sistema.Negocio'),
            preserve_default=False,
        ),
    ]
