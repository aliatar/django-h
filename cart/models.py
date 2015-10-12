import datetime

from django.db import models
from pro.models import pro
from django.contrib.auth.models import User
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User , null=True , blank= True)
    t_peice = models.CharField(max_length = 120 , default = 0)
    active = models.BooleanField(default = True)
    product = models.ManyToManyField(pro, null=True , blank=True)
    time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.id)

