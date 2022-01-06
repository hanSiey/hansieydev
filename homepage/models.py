from django.db import models
from datetime import datetime
# Create your models here.

class ClientMessage(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=1000000)
    date_sent = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
