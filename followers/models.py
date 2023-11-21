from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Model for followers, involving 'owner' and 'followed' entities.
    Using unique_togther stops the user from following another user more than once
    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    started_following = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-started_following']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'