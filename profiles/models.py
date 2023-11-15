from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    profile_avatar = models.ImageField(
        upload_to='images/', default='../defaultUserImage_tuses3'
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.user_profile}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user_profile=instance)

post_save.connect(create_profile, sender=User)
