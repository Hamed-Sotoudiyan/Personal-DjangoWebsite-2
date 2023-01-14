from django.db import models

# Create your models here.

# for example - the imaginary features of employer
class about_detail (models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False)
    title1 = models.TextField(blank=False)
    title2 = models.TextField(blank=False)
    text = models.TextField(blank=False)
    image = models.ImageField(upload_to='about')
    age = models.CharField(max_length=50, blank=False)
    clubhouse = models.CharField(max_length=50, blank=False)
    telegram = models.CharField(max_length=50, blank=False)
    resume = models.FileField(upload_to='about', blank=True)


    def __str__ (self):
        return self.full_name
