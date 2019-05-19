from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField("Date Published", default=datetime.now)
    post_url = models.CharField(max_length=200, default=1)
    summary = models.TextField(default="Summary")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
