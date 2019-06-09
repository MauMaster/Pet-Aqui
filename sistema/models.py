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
from django.conf import settings
from django.db.models import Count, Avg

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
    ('Cachorro','Cachorro'), ('Gato','Gato'), ('Peixes','Peixes'), ('Tartarugas','Tartarugas'), ('Hamster','Hamster')
)

PETN_CHOICES = (
    ('Cachorro','Cachorro'), ('Gato','Gato'), ('Cachorro e  Gato','Cachorro e  Gato')
)

SEXO_CHOICES = (
    ('M','Masculino'), ('F','Feminino')
)

TIPO_CHOICES = (
    ('Hotéis','Hotéis'), ('PetShops','PetShops'), ('Veterinários','Veterinários'), ('Restaurantes','Restaurantes'), ('Cafés','Cafés'), ('HotéisPet','HotéisPet'),
)

HOUR_CHOICES = (
    ('Não','Não'), ('Sim','Sim')
)

NOTA_CHOICES = (
   (0,'0'), (1,'1'), (2,'2'), (3,'3'), (4,'4'), (5,'5')
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
   
    telefone = models.CharField(max_length=20, blank=False)
    cpf = models.CharField(max_length=19)
    data_nascimento = models.CharField(max_length=8, blank=False)
    sexo = models.CharField(default='M', max_length=2, choices=SEXO_CHOICES)
    pet = models.CharField(max_length=255, choices=PETN_CHOICES)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=25)
    cidade = models.CharField(max_length=30)
    estado = models.CharField(default='RS', max_length=3, choices=STATE_CHOICES)
    password1 = models.CharField(max_length=15, blank=False)
    about = models.TextField(max_length=1000, blank=False)


    def __unicode__(self):
	    return self.nome
        
    @receiver(post_save, sender=User)
    def cadastro_novo(sender, instance, created, **kwargs):
        if created:
            Usuario.objects.create(user=instance)
        instance.usuario.save()
        
    def __str__(self):
        return str(self.nome)




class Negocio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=50, blank=False, verbose_name="Nome da Empresa")
    cnpj = models.CharField(max_length=19)
    telefone = models.CharField(max_length=20, blank=False)
    whatsapp = models.CharField(max_length=20, blank=False)
    email = models.EmailField(blank=False)
    site = models.CharField(max_length=50, blank=False)
    foto = StdImageField( blank=False,  variations={
        'large': (600, 400),
        'thumbnail': (100, 100, True),
        'medium': (300, 200),
    })
    tipo = models.CharField( max_length=100, choices=TIPO_CHOICES, verbose_name="Tipo de negocio")
    pet_aceitos = models.CharField(max_length=255, choices=PETN_CHOICES)
    endereco = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=30)
    cep = models.CharField(max_length=25)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(default='RS', max_length=55, choices=STATE_CHOICES)
    segunda = models.CharField(max_length=50, default='Segunda')
    horario_segunda1 = models.TimeField(max_length=50, blank=True, null=True)
    horario_segunda2 = models.TimeField(max_length=50, blank=True, null=True)
    horario_segunda3 = models.TimeField(max_length=50, blank=True, null=True)
    horario_segunda4 = models.TimeField(max_length=50, blank=True, null=True)
    
    terca = models.CharField(max_length=50, default='Terça')
    horario_terca1 = models.TimeField(max_length=50, blank=True, null=True)
    horario_terca2 = models.TimeField(max_length=50, blank=True, null=True)
    horario_terca3 = models.TimeField(max_length=50, blank=True, null=True)
    horario_terca4 = models.TimeField(max_length=50, blank=True, null=True)
    
    quarta = models.CharField(max_length=50, default='Quarta')
    horario_quarta1 = models.TimeField(max_length=50, blank=True, null=True)
    horario_quarta2 = models.TimeField(max_length=50, blank=True, null=True)
    horario_quarta3 = models.TimeField(max_length=50, blank=True, null=True)
    horario_quarta4 = models.TimeField(max_length=50, blank=True, null=True)
    
    quinta = models.CharField(max_length=50, default='Quinta')
    horario_quinta1 = models.TimeField(max_length=50, blank=True, null=True)
    horario_quinta2 = models.TimeField(max_length=50, blank=True, null=True)
    horario_quinta3 = models.TimeField(max_length=50, blank=True, null=True)
    horario_quinta4 = models.TimeField(max_length=50, blank=True, null=True)
    
    sexta = models.CharField(max_length=50, default='Sexta')
    horario_sexta1 = models.TimeField(max_length=50, blank=True, null=True)
    horario_sexta2 = models.TimeField(max_length=50, blank=True, null=True)
    horario_sexta3 = models.TimeField(max_length=50, blank=True, null=True)
    horario_sexta4 = models.TimeField(max_length=50, blank=True, null=True)
   
    sabado = models.CharField(max_length=50, default='Sábado')
    horario_sabado1 = models.TimeField(max_length=50, blank=True, null=True)
    horario_sabado2 = models.TimeField(max_length=50, blank=True, null=True)
    horario_sabado3 = models.TimeField(max_length=50, blank=True, null=True)
    horario_sabado4 = models.TimeField(max_length=50, blank=True, null=True)
    
    domingo = models.CharField(max_length=50, default='Domingo')
    horario_domingo1 = models.TimeField(max_length=50, blank=True, null=True)
    horario_domingo2 = models.TimeField(max_length=50, blank=True, null=True)
    horario_domingo3 = models.TimeField(max_length=50, blank=True, null=True)
    horario_domingo4 = models.TimeField(max_length=50, blank=True, null=True)
    
    sobre = models.TextField(max_length=1000, blank=False)
    password1 = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return str(self.empresa) + ' - ' + str(self.email) + ' - ' + str(self.whatsapp) + ' - ' + str(self.cnpj) 

  

    @receiver(post_save, sender=User)
    def cadastro_negocio_novo(sender, instance, created, **kwargs):
        if created:
            Negocio.objects.create(user=instance)
        instance.negocio.save()


class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    file = StdImageField( upload_to='photos/', blank=False,  variations={
        'large': (900, 700),
        'thumbnail': (100, 100, True),
        'medium': (300, 200),
    })
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Pets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pets = MultiSelectField(max_length=255, choices=PET_CHOICES)


class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=255, blank=False)
    comentario = models.TextField(max_length=255, blank=False)
    nota = models.IntegerField( choices=NOTA_CHOICES, null=True, blank=True)


    def __str__(self):
        return str(self.empresa)

    def clean(self):
        if self.nota is None:
            self.nota = 0

 
    
    
    
    