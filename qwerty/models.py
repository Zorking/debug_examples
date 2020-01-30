from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=255)


class Order(models.Model):
    name = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    ...
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Films(models.Model):
    nconst = models.CharField(max_length=3000, blank=True)
    primaryName = models.CharField(max_length=3000, blank=True)
    birthYear = models.CharField(max_length=3000, blank=True)
    deathYear = models.CharField(max_length=3000, blank=True)
    primaryProfession = models.CharField(max_length=3000, blank=True)
    knownForTitles = models.CharField(max_length=3000, blank=True)
