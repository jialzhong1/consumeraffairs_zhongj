from django.db import models

class Event(models.Model):

    session_id = models.CharField(max_length = 100, default=None)
    category = models.CharField(max_length = 50, default=None)
    name = models.CharField(max_length = 50, default=None)
    data = models.JSONField(default=dict)
    timestamp = models.DateField()
    has_errors = models.BooleanField(default=False) # Added this field to better filter for errors if needed
