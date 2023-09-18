from django.db import models
from django.urls import reverse
# Create your models here.
class NewServices(models.Model):
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=1000)

    def get_absolute_urls(self):
        return reverse('details', kwargs={'id':self.id})

class Blogs(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=10000)
    content = models.CharField(max_length=1000000)   

    def get_absolute_urls(self):
        return reverse('single', kwargs={id:self.id}) 

