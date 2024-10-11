from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
# from django.urls import reverse

# Create your models here.

class Task(models.Model):
    content = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    complete = models.BooleanField(default=False)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.content

    # def get_absolute_url(self):
    #     return reverse("post-detail", kwargs={'pk': self.pk})
