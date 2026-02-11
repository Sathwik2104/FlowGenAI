# flow_generator/models.py
from django.db import models

class Flow(models.Model):
    topic = models.CharField(max_length=200)
    content = models.TextField()  # The generated flow text
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic