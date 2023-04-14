from django.db import models
from django.urls import reverse

# Create your models here.
# class Companion(models.Model):
#     name = models.CharField(max_length=75)
#     relation = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

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

class Comment(models.Model):
    date = models.DateField(auto_now_add=True)
    author = models.CharField('your name', max_length=75)
    content = models.TextField('comment')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on {self.date}"

    class Meta:
        ordering = ['-date']