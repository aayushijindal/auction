from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import datetime

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, null=True,verbose_name=_('First name'))
    lastname = models.CharField(max_length=100, null=True,verbose_name=_('Last name'))
    email = models.EmailField(max_length=20, blank=True, null=True,verbose_name=_('Email'))
    phone = models.CharField(max_length=10, blank=True, null=True,verbose_name=_('Phone'))

    # def __str__(self):
    #     return self.user.username

    def __str__(self):
        return self.firstname



class Contact(models.Model):
    c_name = models.CharField(max_length=100,verbose_name=_('Name'))
    c_email = models.EmailField(max_length=100,verbose_name=_('Email'))
    c_subject = models.CharField(max_length=100,verbose_name=_('Subject'))
    c_message = models.TextField(verbose_name=_('Message'))
    
