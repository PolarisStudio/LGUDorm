from django.db import models
from django.utils import timezone

# Create your models here.

class Record(models.Model):
    time = models.fields.DateTimeField(auto_now_add=True)
    college = models.fields.CharField(max_length=32, choices = (('逸夫', '逸夫'), ('学勤','学勤'), ('思廷', '思廷'), ('祥波', '祥波')))
    note = models.fields.TextField(max_length=256)
    contact = models.fields.TextField(max_length=100)
    available = models.fields.BooleanField(default=True)
    IPadd = models.fields.CharField(max_length = 30, default = "")
    IPdelete = models.fields.CharField(max_length = 30, default="")


