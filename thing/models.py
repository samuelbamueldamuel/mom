from django.db import models

class Task(models.Model):
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    point = models.IntegerField()
    chosen = models.BooleanField(default=False)

class History(models.Model):
    key = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    point = models.IntegerField()
    accepted = models.BooleanField()
# Create your models here.
