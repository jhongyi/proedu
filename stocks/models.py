from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Stock(models.Model):
    '''
    stocks
    '''
    number = models.IntegerField()
    stock_name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "stock"
