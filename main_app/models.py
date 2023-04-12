from django.db import models

# Create your models here.
class Ticket(models.Model):
    event: models.CharField(max_length=150)
    highlight: models.TextField
    date: models.DateField
    venue: models.CharField(max_length=150)

    def __str__(self):
        return self.event