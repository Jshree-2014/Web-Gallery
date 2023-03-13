from distutils.command.upload import upload
from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(primary_key=True,max_length=25)
    realname=models.CharField(max_length=40)
    emailid=models.CharField(max_length=60)
    password=models.CharField(max_length=16,)
    
class Gallery(models.Model):
    title=models.CharField(max_length=100)
    user=models.CharField(max_length=40,default="admin")
    #category=models.CharField(max_length=40)
    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='images/')

class Video(models.Model):
    title=models.CharField(max_length=100)
    user=models.CharField(max_length=40,default="admin")
    date=models.DateTimeField(auto_now_add=True) 
    video=models.FileField(upload_to='video/%y')


