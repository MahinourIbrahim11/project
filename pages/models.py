from django.db import models

# Create your models here.
class car (models.Model):
    username = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='car_images/%y/%m/%d/', null=True, blank=True)
    active = models.BooleanField(default=True)


class Form (models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username