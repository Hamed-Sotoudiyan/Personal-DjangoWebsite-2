from django.db import models

# Create your models here.

class Notes (models.Model):
    date = models.CharField(max_length=50, blank=False)
    title = models.TextField(blank=False)
    text = models.TextField(blank=False)
    image = models.ImageField(upload_to='note', blank=False, null=True)
    note_url = models.URLField(max_length=300,blank=True)
    is_note_url = models.BooleanField(default=False, blank=False)

    def __str__ (self):
        return self.title
