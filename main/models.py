from django.contrib.auth.models import *
from django.db import models

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, null=True)
    number = models.CharField(max_length=15, unique=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=20)
    is_spam = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user'


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True)
    number = models.CharField(max_length=15, blank=False, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_spam = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'contact'

class SpamContact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True)
    number = models.CharField(max_length=15, blank=False, null=True)
    is_spam = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'spam_contact'




