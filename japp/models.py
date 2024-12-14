from django.db import models
class student(models.Model):
    first_name=models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(unique=True)
    address=models.TextField()


# Create your models here.
def __str__(self):
        return self.first_name