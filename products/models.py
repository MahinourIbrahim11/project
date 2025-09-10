from django.db import models

class Product(models.Model):
    x=(('food','food'),('clothes','clothes'),('electronics','electronics'),('books','books'),('other','other'))
    name = models.CharField(max_length=255, verbose_name='Product Name')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=100, blank=True, null=True,choices=x, help_text='select a category for the product')
    

    

class Test(models.Model):
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)