from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to="images/", null=True, blank=True)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


