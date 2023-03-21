from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=20, null=False)
    email= models.EmailField(null=False)
    phone=models.IntegerField( null=False)
    message=models.CharField(max_length=200, null=False)

    def __str__(self) :
        return '%s %s %s' %(self.name, self.phone, self.email)
    