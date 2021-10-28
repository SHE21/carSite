from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField('Nome Membro', max_length=100)
    degree = models.CharField('Habilitação', max_length=200)
    descript = models.CharField('Descrição do Membro', max_length=200)
    thumb = models.CharField('Foto', max_length=50)


class Service(models.Model):
    title = models.CharField('Nome Serviço', max_length=100)
    descript = models.CharField('Descrição do Serviço', max_length=300)
    icon = models.CharField('Icone', max_length=50)


class Contact(models.Model):
    name = models.CharField('Nome Cliente', max_length=100)
    email = models.EmailField('Email Cliente', max_length=100)
    phone = models.CharField('Telefone', max_length=50)
    message = models.TextField('Menssagem')
