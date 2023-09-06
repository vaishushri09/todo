from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, default="")  # Default title is an empty string
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)  # Default completed status is False
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
