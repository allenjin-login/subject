# Create your models here.
from django.db import models


# Create your models here.
class Apply(models.Model):
    sid = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=50)
    add_time = models.DateField(auto_now_add=True)
