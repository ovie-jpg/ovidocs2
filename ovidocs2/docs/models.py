from email.mime import image
from multiprocessing.sharedctypes import Value
from turtle import position
from django.db import models
from django.urls import reverse
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class Details(models.Model):
    pic = models.ImageField()
    fname = models.CharField(max_length=250)
    lname = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.IntegerField()
    author = models.ForeignKey(User, on_delete= models.CASCADE, null= True, blank= True)

    def get_absolute_url(self):
        return reverse('formlist')




class Address(models.Model):
    snum = models.IntegerField()
    stname = models.CharField(max_length=250)
    lgname = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete= models.CASCADE, null= True, blank= True)

    def get_absolute_url(self):
        return reverse('formlist')

class Objectives(models.Model):
    car = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE, null= True, blank= True)

    def get_absolute_url(self):
        return reverse('formlist')

class Education(models.Model):
    inst = models.CharField(max_length=250)
    location = models.TextField()
    start = models.IntegerField()
    end = models.IntegerField()
    cert = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete= models.CASCADE, null= True, blank= True)

    def get_absolute_url(self):
        return reverse('formlist')


class Works(models.Model):
    name = models.CharField(max_length=250)
    location = models.TextField()
    start = models.IntegerField()
    end = models.IntegerField()
    author = models.ForeignKey(User, on_delete= models.CASCADE, null= True, blank= True)

    def get_absolute_url(self):
        return reverse('formlist')

class Roles(models.Model):
    names = models.TextField()

class Skills(models.Model):
    names = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE, null= True, blank= True)

    def get_absolute_url(self):
        return reverse('formlist')
        


class References(models.Model):
    name = models.CharField(max_length=250)
    firm = models.CharField(max_length=250)
    tel = models.IntegerField()
    email = models.EmailField()
    author = models.ForeignKey(User, on_delete= models.CASCADE, null= True, blank= True)

    def get_absolute_url(self):
        return reverse('formlist')

class Jobs(models.Model):
    firm = models.CharField(max_length=250)
    location = models.TextField()
    req = models.TextField(default= 'none stated')
    position = models.TextField()


class Duties(models.Model):
    resp = models.TextField()
     