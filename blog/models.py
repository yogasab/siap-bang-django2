from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.TextField(max_length=50)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    # To send data and get back to post_detail.html
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])