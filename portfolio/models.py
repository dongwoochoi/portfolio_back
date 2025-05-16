from django.db import models
class Post(models.Model):
        writer = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
# Create your models here.
