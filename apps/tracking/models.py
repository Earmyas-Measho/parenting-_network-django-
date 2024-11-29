from django.db import models

class Tracking(models.Model):
    user_id = models.IntegerField()
    action = models.CharField(max_length=200)
