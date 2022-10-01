from django.db import models
from django.utils.timezone import now
# Create your models here.

class Ask(models.Model):
    qid = models.CharField(max_length=1000 , null=False , primary_key=True)
    question = models.CharField (max_length=250 , null=False)
    description = models.TextField(max_length=1000 , null=False)
    datetime = models.DateTimeField(now() , auto_now=True)
    def __str__(self):
        return self.question