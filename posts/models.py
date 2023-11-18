from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model related to the user.
    User can upload images and videos in a post and will be linked to the users account
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    post_header = models.CharField(max_length=255)
    caption = models.TextField(blank=True)
    upload = models.FileField(
        upload_to='files/', default='../default_post_ns8zax', blank=True
    )


    class Meta:
        ordering = ['-uploaded_on']

    def __str__(self):
        return f'{self.id} {self.post_header}'
