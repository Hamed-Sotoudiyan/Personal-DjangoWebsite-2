from django.db import models

# Create your models here.

class Home (models.Model):
    title1 = models.TextField(blank=False)
    title2 = models.TextField(blank=False)

    def __str__ (self):
        return self.title1
