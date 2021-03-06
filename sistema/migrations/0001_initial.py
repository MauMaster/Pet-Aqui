# Generated by Django 2.1.7 on 2019-04-03 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Negocio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=50, verbose_name='Nome da Empresa')),
                ('cnpj', models.CharField(max_length=19)),
                ('telefone', models.CharField(max_length=20)),
                ('whatsapp', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('site', models.CharField(max_length=50)),
                ('foto', stdimage.models.StdImageField(upload_to='')),
                ('tipo', multiselectfield.db.fields.MultiSelectField(choices=[('Hotéis', 'Hotéis'), ('PetShops', 'PetShops'), ('Veterinários', 'Veterinários'), ('Restaurantes', 'Restaurantes'), ('Cafés', 'Cafés'), ('HotéisPet', 'HotéisPet')], max_length=100, verbose_name='Tipo de negocio')),
                ('pet_aceitos', multiselectfield.db.fields.MultiSelectField(choices=[('Cachorro', 'Cachorro'), ('Gato', 'Gato'), ('Pássaros', 'Pássaros'), ('Peixes', 'Peixes'), ('Reptéis', 'Reptéis'), ('Roedores', 'Roedores')], max_length=255)),
                ('endereco', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=30)),
                ('cep', models.CharField(max_length=25)),
                ('cidade', models.CharField(max_length=20)),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='RS', max_length=55)),
                ('segunda', models.CharField(default='Segunda', max_length=50)),
                ('horario_segunda1', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_segunda2', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_segunda3', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_segunda4', models.TimeField(blank=True, max_length=50, null=True)),
                ('segunda_24', models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='N', max_length=3)),
                ('terca', models.CharField(default='Terça', max_length=50)),
                ('horario_terca1', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_terca2', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_terca3', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_terca4', models.TimeField(blank=True, max_length=50, null=True)),
                ('terca_24', models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='N', max_length=3)),
                ('quarta', models.CharField(default='Quarta', max_length=50)),
                ('horario_quarta1', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_quarta2', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_quarta3', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_quarta4', models.TimeField(blank=True, max_length=50, null=True)),
                ('quarta_24', models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='N', max_length=3)),
                ('quinta', models.CharField(default='Quinta', max_length=50)),
                ('horario_quinta1', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_quinta2', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_quinta3', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_quinta4', models.TimeField(blank=True, max_length=50, null=True)),
                ('quinta_24', models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='N', max_length=3)),
                ('sexta', models.CharField(default='Sexta', max_length=50)),
                ('horario_sexta1', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_sexta2', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_sexta3', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_sexta4', models.TimeField(blank=True, max_length=50, null=True)),
                ('sexta_24', models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='N', max_length=3)),
                ('sabado', models.CharField(default='Sábado', max_length=50)),
                ('horario_sabado1', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_sabado2', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_sabado3', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_sabado4', models.TimeField(blank=True, max_length=50, null=True)),
                ('sabado_24', models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='N', max_length=3)),
                ('domingo', models.CharField(default='Domingo', max_length=50)),
                ('horario_domingo1', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_domingo2', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_domingo3', models.TimeField(blank=True, max_length=50, null=True)),
                ('horario_domingo4', models.TimeField(blank=True, max_length=50, null=True)),
                ('domingo_24', models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], default='N', max_length=3)),
                ('sobre', models.TextField(max_length=1000)),
                ('password1', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254)),
                ('foto', stdimage.models.StdImageField(upload_to='')),
                ('telefone', models.CharField(max_length=20, verbose_name='Celular')),
                ('cpf', models.CharField(max_length=19)),
                ('data_nascimento', models.CharField(max_length=8, verbose_name='Data de nascimento')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', max_length=2)),
                ('pet', multiselectfield.db.fields.MultiSelectField(choices=[('Cachorro', 'Cachorro'), ('Gato', 'Gato'), ('Pássaros', 'Pássaros'), ('Peixes', 'Peixes'), ('Reptéis', 'Reptéis'), ('Roedores', 'Roedores')], max_length=100, verbose_name='Selecione seus pets')),
                ('endereco', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=30)),
                ('cep', models.CharField(max_length=25)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], default='RS', max_length=3)),
                ('password1', models.CharField(max_length=15)),
                ('about', models.TextField(max_length=1000, verbose_name='Sobre você')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
