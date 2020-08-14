from django.db import models
from tinymce.models import HTMLField

class Article(models.Model):
        title = models.CharField(max_length = 120)
        text = HTMLField()
        date = models.DateTimeField()
        image = models.ImageField(upload_to = "images/")