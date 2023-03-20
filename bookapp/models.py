from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
