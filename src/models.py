from django.db import models

# Create your models here.
class Products(models.Model):
    name        = models.CharField(max_length=100)
    vendor      = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image       = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Products'
        verbose_name_plural = 'Products'