from django.db import models

class computer(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return f"{self.brand} {self.name} - ${self.price}"