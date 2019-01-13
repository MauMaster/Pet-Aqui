from django.db import models
from django.core.files.images import ImageFile
from django.core.mail import send_mail
import math
from multiselectfield import MultiSelectField


STATE_CHOICES = (
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'),
    ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
    ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
)

PET_CHOICES = (
    ('dog','Cachorro'), ('cat','Gato'), ('bird', 'Pássaros'), ('fish','Peixes'), ('rep','Reptéis'), ('naosei','Cavalos'), ('rat','Roedores')
)


SEXO_CHOICES = (
    ('M','Masculino'), ('F','Feminino')
)


class Usuario(models.Model):
    
    nome = models.CharField(max_length=50, blank=False)
    sobrenome = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True,blank=False)
    foto = models.ImageField( blank=False)
    telefone = models.CharField(max_length=20, blank=False)
    cpf = models.CharField(unique=True, max_length=19)
    data_nascimento = models.CharField(max_length=8, blank=False)
    sexo = models.CharField(default='M', max_length=2, choices=SEXO_CHOICES)
    pet = MultiSelectField( max_length=30, choices=PET_CHOICES)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=25)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(default='RS', max_length=2, choices=STATE_CHOICES)
    senha = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return str(self.nome) + ' - ' + str(self.email) + ' - ' + str(self.telefone) 


class Negocio(models.Model):
    id = models.AutoField(primary_key=True)
    responsavel =  models.ForeignKey( Usuario, on_delete=models.CASCADE, blank=False)
    estabelecimento = models.CharField(max_length=50, blank=False)
    telefone = models.CharField(max_length=20, blank=False)
    site = models.CharField(max_length=50, blank=False)
    foto = models.ImageField(height_field=500, width_field=500, upload_to='foto_estabelecimento')
    pet_aceitos = models.CharField(default='dog', max_length=2, choices=PET_CHOICES)
    horario = models.CharField(max_length=50, blank=False)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=25)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(default='RS', max_length=2, choices=STATE_CHOICES)
    senha = models.CharField(max_length=15, blank=False)
