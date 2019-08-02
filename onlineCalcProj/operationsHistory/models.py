from django.db import models
import datetime
from datetime import *

class History(models.Model):
       expression = models.CharField(max_length=1000)
       ans = models.CharField(max_length=1000,null=True)
       error = models.CharField(max_length=100,null=True)
       updated_at=models.DateTimeField('Uploaded at',default=datetime.now,editable=False)
       class Meta:
              db_table = 'history'       

