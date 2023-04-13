from django.db import models
from django.urls import reverse

# Create your models here.
class Ticket(models.Model):
    event = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    date = models.DateField()
    location = models.CharField(max_length=150)

    def __str__(self):
        return self.event
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'ticket_id': self.id})
    
    class Meta:
        ordering = ['-date']