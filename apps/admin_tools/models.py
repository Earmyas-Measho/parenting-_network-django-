from django.db import models

class AdminTool(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
