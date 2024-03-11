from django.db import models

class Dragon(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    hyper = models.IntegerField()
    hunger = models.IntegerField()