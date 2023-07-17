from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.TextField()
    author = models.TextField()
    overview = models.TextField()
    image = models.TextField()
    url = models.TextField()