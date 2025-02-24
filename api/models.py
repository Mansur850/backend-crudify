from django.db import models
from datetime import datetime

class Item(models.Model):
    content = models.TextField()
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)


# Create your models here.
