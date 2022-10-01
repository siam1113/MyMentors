from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils.timezone import now
# Create your models here.

class Answer(models.Model):
    qid = models.ForeignKey("Ask.Ask" , on_delete=models.CASCADE)
    answer = models.TextField()
    name = models.ForeignKey("Mentors.Mentor" , on_delete=models.CASCADE)
    datetime = models.DateTimeField(now())

    def __str__(self):
        return self.qid.question

class Post(models.Model):
    pid = models.CharField(primary_key=True, max_length=1000 , default=0)
    author = models.ForeignKey("Mentors.Mentor" , on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    post = models.TextField()
    datetime = models.DateTimeField(now())

    def __str__(self):
        return self.title

