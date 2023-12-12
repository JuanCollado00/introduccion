from django.db import models

# Create your models here.

class post(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()

    def __str__(self):
        return self.title,self.content

class secondpost(models.Model):
    ejemplo=models.TextField()    
    

class tercero(models.Model):
    title3=models.CharField(max_length=250)
    content3=models.TextField()

    def __str__(self):
        return self.title3,self.content3
    
    
