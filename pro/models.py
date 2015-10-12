from django.db import models

# Create your models here.

class pro(models.Model):
    name = models.CharField(max_length = 120)
    des = models.CharField(max_length=300, blank=True, null=True )
    slug = models.SlugField()

    def __str__(self):
        return self.name
