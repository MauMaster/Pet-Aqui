from django.db import models
from django.core.files.images import ImageFile
from django.core.mail import send_mail
import math
from multiselectfield import MultiSelectField
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from stdimage.models import StdImageField

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

cat = 'https://www.petz.com.br/blog/wp-content/uploads/2017/07/gato02.jpg'
gato = 'https://www.petz.com.br/blog/wp-content/uploads/2017/07/gato02.jpg'
PET_CHOICES = (
    ('dog','Cachorro'), ('cat','Gato'), ('bird', 'Pássaros'), ('fish','Peixes'), ('rep','Reptéis'), ('horse','Cavalos'), ('rat','Roedores')
)


SEXO_CHOICES = (
    ('M','Masculino'), ('F','Feminino')
)


class Usuario(models.Model):
    
    nome = models.CharField(max_length=50, blank=False)
    sobrenome = models.CharField(max_length=50, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    email = models.EmailField(blank=False)
    foto = StdImageField( blank=False,  variations={
        'large': (600, 400),
        'thumbnail': (100, 100, True),
        'medium': (300, 200),
    })
    telefone = models.CharField(max_length=20, blank=False, verbose_name="Celular")
    cpf = models.CharField(max_length=19)
    data_nascimento = models.CharField(max_length=8, blank=False, verbose_name="Data de nascimento")
    sexo = models.CharField(default='M', max_length=2, choices=SEXO_CHOICES)
    pet = MultiSelectField( max_length=30, choices=PET_CHOICES, verbose_name="Selecione seus pets")
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=25)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(default='RS', max_length=3, choices=STATE_CHOICES)
    password1 = models.CharField(max_length=15, blank=False)

    
    def __unicode__(self):
	    return self.nome
        
    @receiver(post_save, sender=User)
    def cadastro_novo(sender, instance, created, **kwargs):
        if created:
            Usuario.objects.create(user=instance)
        instance.usuario.save()
        
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

    