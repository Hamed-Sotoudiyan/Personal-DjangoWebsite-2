from django.db import models

# Create your models here.

# for example - the imaginary features of Articles

class Articles (models.Model):
    date = models.CharField(max_length=50, blank=False)
    title = models.TextField(blank=False)
    publisher = models.CharField(max_length=50, blank=False)
    abstract = models.TextField(blank=False)
    article = models.FileField(upload_to='article')
    article_url = models.URLField(max_length=300,blank=True)
    is_article_url = models.BooleanField(default=False, blank=False)

    def __str__ (self):
        return self.title
