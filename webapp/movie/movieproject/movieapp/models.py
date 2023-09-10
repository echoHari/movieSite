from django.db import models


# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    desc = models.TextField()
    img = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
