from django.db import models
from django.utils import timezone

class communities(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(max_length=150)
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)
    free = models.BooleanField(default=False)

    def __str__(self):
           return self.name
# Create your models here.

  