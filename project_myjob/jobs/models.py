from django.db import models
import datetime

# Create your models here.
class Job(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title