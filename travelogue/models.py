from django.db import models

# Create your models here.

# for example - the imaginary features of Travelogue

class Travelogue (models.Model):
    date = models.CharField(max_length=50, blank=False)
    title = models.TextField(blank=False)
    text = models.TextField(blank=False)
    province = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)
    image_one = models.ImageField(upload_to='Travelogue', blank=False, null=True)
    image_two = models.ImageField(upload_to='Travelogue', blank=False, null=True)

    def __str__ (self):
        return self.title

class Images (models.Model):
    image = models.ImageField(upload_to='Travelogue',blank=True)
    travelogue_id = models.ForeignKey(Travelogue,on_delete=models.CASCADE)
