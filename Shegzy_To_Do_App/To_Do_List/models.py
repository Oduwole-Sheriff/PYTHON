from django.db import models
from django.utils import timezone
from django.urls import reverse

# Register your models here.
class Post(models.Model):
    content = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content