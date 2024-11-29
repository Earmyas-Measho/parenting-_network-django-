from django.db import models

class Community(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
