# flow_generator/models.py
from django.db import models
from django.contrib.auth.models import User

class Flow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    topic = models.CharField(max_length=200)
    content = models.TextField()  # The generated flow text
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.topic