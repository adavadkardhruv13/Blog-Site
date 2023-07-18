from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=13)
    content = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return "message from " + self.name


