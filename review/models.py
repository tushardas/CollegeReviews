from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#model for user login
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #password = models.CharField(null=0False, max_length=128)
    #website = models.URLField(blank = True)

    def __unicode__(self):
        return self.user.username

#model for College details
class College(models.Model):
    name = models.CharField(unique=True, null=False, max_length=128)
    location = models.CharField(null=False, max_length=128)
    principles = models.CharField(null=False, max_length=128)                   #be, btech, medical , etc.

    def __unicode__(self):
        return self.name

#model for storing file for each College inorder to store reviews
class FileInfo(models.Model):
    collname = models.ForeignKey(College)
    filename = models.CharField(null=False, max_length=128)

    def __unicode__(self):
        return self.collname.name