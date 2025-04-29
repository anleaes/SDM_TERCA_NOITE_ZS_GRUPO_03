from django.db import models



class Client(models.Model):
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100) 
    address = models.CharField('Endereco', max_length=200)   
    cell_phone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)

    def client_socialNetwork(self):
        from clientsocialnetwork.models import ClientSocialNetwork
        return models.ManyToManyField('socialnetworks.SocialNetwork', through=ClientSocialNetwork, blank=True)

        
    class Meta:
        app_label = 'clients'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']
        

    def __str__(self):
        return self.first_name

