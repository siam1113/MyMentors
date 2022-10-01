from django.db import models

# Create your models here.
class Mentor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="images")
    about = models.TextField()
    link = models.CharField(max_length=200)
    def __str__(self):
        return self.name