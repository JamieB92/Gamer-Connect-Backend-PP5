from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):

    """
    Profile Model that alows the user to select prefered
    platform they play on with the platforms usename.
    Default profile avatar set
    """

    xbox = 'Xbox'
    playstation = 'Playstation'
    steam = 'Steam'
    nswitch = 'Nintendo Switch'
    discord = 'Discord'

    preferred_platform = [
        (xbox, 'Xbox'),
        (playstation, 'Playstation'),
        (steam, 'Steam'),
        (nswitch, 'Nintendo Switch'),
        (discord, 'Discord'),
    ]

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    platform = models.CharField(
        'Preferred Platform', max_length=20, blank=True,
        choices=preferred_platform
    )
    platform_username = models.CharField(
        'Platform Username', max_length=255, blank=True)
    profile_avatar = models.ImageField(
        upload_to='images/', default='../defaultUserImage_tuses3'
    )
    game_id = models.IntegerField(null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
