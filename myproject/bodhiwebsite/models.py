from django.db import models

# Create your models here.

class carousel(models.Model):
    heading=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=200,null=True)
    img=models.ImageField(upload_to="img/carousel",null=True)
    submitted_at= models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"carousel"


class features(models.Model):
    heading=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=200,null=True)
    img=models.ImageField(upload_to="img/icon",null=True)
    submitted_at= models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"features"


class client(models.Model):
    heading=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=200,null=True)
    img=models.ImageField(upload_to="img/icon",null=True)
    submitted_at= models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)

    class Meta:
        db_table:"client"
        
class about(models.Model):
    heading=models.CharField(max_length=50,null=True)
    description1=models.CharField(max_length=200,null=True)
    description2=models.CharField(max_length=200,null=True)
    description3=models.CharField(max_length=200,null=True)
    img=models.ImageField(upload_to="img/icon",null=True)
    submitted_at= models.DateTimeField(auto_now_add=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table:"about"

     
    def __str__(self): 
        return self.heading 

