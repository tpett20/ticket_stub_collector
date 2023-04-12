from django.db import models

# Create your models here.
class Ticket(models.Model):
    event = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    date = models.DateField()
    location = models.CharField(max_length=150)

    def __str__(self):
        return self.event