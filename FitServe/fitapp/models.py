from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122,null=True,blank=True)
    email= models.CharField(max_length=122,null=True,blank=True)
    phone= models.CharField(max_length=12,null=True,blank=True)
    desc= models.TextField(null=True,blank=True)
    date= models.DateField(null=True,blank=True)

    def __str__(self):
        return self.name

class Members(models.Model):
    Name = models.CharField(max_length=122,null=True,blank=True)
    Email= models.CharField(max_length=122,null=True,blank=True)
    Phone= models.CharField(max_length=12,null=True,blank=True)
    Date= models.DateField(null=True,blank=True)

    def __str__(self):
        return self.Name

