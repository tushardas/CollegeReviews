from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

#model for College details
class Coll(models.Model):
    name = models.CharField(unique=True, null=False, max_length=128)
    location = models.CharField(null=False, max_length=128)
    principles = models.CharField(null=False, max_length=128)                   #be, btech, medical , etc.
    clubs = models.CharField(null=False, max_length=128)
    sports = models.CharField(null=False, max_length=128)

    def __unicode__(self):
        return self.name

#model for storing file for each College inorder to store reviews

class UserDetails(models.Model):
    username = models.CharField(unique=True, null=False, max_length=128)
    email = models.CharField(unique=False, null=False, max_length=128)
    password = models.CharField(unique=False, null=False, max_length=128)

    def __unicode__(self):
        return self.username

class FileInfo(models.Model):
    collname = models.ForeignKey(Coll)
    filename = models.CharField(null=False, max_length=128)

    def __unicode__(self):
        return self.collname.name