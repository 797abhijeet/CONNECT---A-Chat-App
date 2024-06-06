from django.db import models
from datetime import datetime

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=500)

class Message(models.Model):
    group = models.CharField(max_length=500)
    user = models.CharField(max_length=500)
    msg = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
