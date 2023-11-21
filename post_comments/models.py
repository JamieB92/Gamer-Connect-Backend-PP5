from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    """
    Post comments model related to the User and the Posts created
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.comment
