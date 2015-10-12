from django.db import models
import datetime
# Create your models here.

class contactus(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 250)
    msg = models.CharField(max_length = 500)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
