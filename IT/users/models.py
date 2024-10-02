import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save,post_delete
from django.dispatch import Signal,receiver

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(null=True,blank=True,max_length=200)
    info = models.CharField(null=True,blank=True,max_length=200)
    location = models.CharField(max_length=300,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    social_github = models.CharField(max_length=200,null=True,blank=True)
    social_instagram = models.CharField(max_length=200,null=True,blank=True)
    social_telegram = models.CharField(max_length=200,null=True,blank=True)
    social_linkedin = models.CharField(max_length=200,null=True,blank=True)
    social_facebook = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='profile_photos',default='profile_photos/default_profile.webp',null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self) -> str:
        return str(self.user)

class Skill(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True,related_name='skills')
    name = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    def __str__(self) -> str:
        return str(self.name)

