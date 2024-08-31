from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    logo = models.CharField(max_length=200)
    slug = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name


class Slider(models.Model):
    name = models.CharField(max_length=300, unique=True)
    image = models.ImageField(upload_to='media')
    rank = models.IntegerField()
    description = models.TextField(blank=True)
    url = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media')
    rank = models.IntegerField()

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='media')
    slug = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=100)
    star = models.IntegerField()
    image = models.ImageField(upload_to='media')
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.name


LABEL = (('default', 'default'), ('New', 'New'), ('Hot', 'Hot'), ('Sale', 'Sale'))
STOCK = (('IN STOCK', 'IN STOCK'), ('OUT OF STOCK', 'OUT OF STOCK'))


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_star = models.IntegerField()
    product_image = models.ImageField(upload_to='product_images')
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    description = models.TextField()
    specification = models.TextField(blank=True)
    slug = models.SlugField(max_length=300, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True)
    stock = models.CharField(max_length=100, choices=STOCK)
    label = models.CharField(max_length=100, choices=LABEL)

    def __str__(self):
        return self.product_name
