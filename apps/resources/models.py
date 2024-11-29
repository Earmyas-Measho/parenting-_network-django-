from django.db import models

class Resource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    class Meta:
        app_label = 'resources'

    def __str__(self):
        return self.title
