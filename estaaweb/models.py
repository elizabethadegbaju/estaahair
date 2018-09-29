from django.db import models
from django.utils import timezone

# Create your models here.

class Hair (models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'estaaweb/static/img')
    length = models.CharField(max_length=200)
    weight = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def buy(self, n):
        self.quantity = self.quantity-n
        self.save()

    def __str__(self):
        return self.name


class Appliance(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='estaaweb/static/img')
    quantity = models.IntegerField()
    price = models.IntegerField()

    def buy(self, n):
        self.quantity = self.quantity - n
        self.save()

    def __str__(self):
        return self.name


class WigEssential(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='estaaweb/static/img')
    quantity = models.IntegerField()
    price = models.IntegerField()

    def buy(self, n):
        self.quantity = self.quantity - n
        self.save()

    def __str__(self):
        return self.name


class HairAccessory(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='estaaweb/static/img')
    quantity = models.IntegerField()
    price = models.IntegerField()

    def buy(self, n):
        self.quantity = self.quantity - n
        self.save()

    def __str__(self):
        return self.name


class Post (models.Model):
    author = models.ForeignKey('auth.User', on_delete = 'cascade')
    title = models.CharField(max_length = 200)
    text = models.TextField()
    image = models.ImageField(upload_to = 'estaaweb/static/img')
    created_date = models.DateTimeField(default = timezone.now())
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Review (models.Model):
    customer = models.CharField(max_length = 200)
    comment = models.TextField()
    image = models.ImageField(upload_to = 'estaaweb/static/img')
    product = models.ForeignKey('estaaweb.Hair', on_delete = 'cascade')

    def __str__(self):
        return self.customer

