from email.policy import default
import uuid
from django.db import models
from django.dispatch import Signal
from users.models import Profile
from django.db.models.signals import post_save
class Project(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True,blank=True,related_name='projects')
    title = models.CharField(max_length=300)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='project_images')
    demo_link = models.CharField(max_length=400,null=True,blank=True)
    source_link = models.CharField(max_length=400,null=True,blank=True)
    vote_count = models.IntegerField(default=0)
    vote_radio = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    tag = models.ManyToManyField('Tag',blank=True,related_name='project_tag')
    def __str__(self) -> str:
        return self.title
    

class Review(models.Model):

    VOTE_TYPE = (
        ("+","Ijobiy"),
        ("-","Salbiy")
    )
    body = models.TextField(default='')
    value = models.CharField(max_length=50,choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,null=True,blank=True,related_name="project_review")

    def __str__(self) -> str:
        return self.value
    
class Tag(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    
    def __str__(self) -> str:
        return self.name
    


