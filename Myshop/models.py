from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50)
    categories = models.ManyToManyField(Category, related_name='products')
    sku = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    qty = models.IntegerField()
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title
