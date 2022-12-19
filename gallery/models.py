from django.db import models

# Create your models here.

class Gallery (models.Model):
    date = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='gallery')

    def __str__ (self):
        return self.title
