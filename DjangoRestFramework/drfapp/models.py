from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    date_enrolled = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name