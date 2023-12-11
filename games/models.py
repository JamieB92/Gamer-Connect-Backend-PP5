from django.db import models
from profiles.models import Profile
from django.contrib.auth.models import User

class Games(models.Model):
    """
    Games model category that links to the Profile model
    Allows user to diplay what games they are currently playing
    """

    yes = 'Yes'
    no = 'No'

    noob = 'Noob'
    casual = 'Casual'
    pro = 'Pro'
    veteran = 'Vetran'
    master = 'Master'
    god = 'God'


    looking_for_friends_choice = [
        (yes, 'Yes'),
        (no, 'No'),
    ]

    experience_level = [
        (noob, 'Noob'),
        (casual, 'Casual'),
        (pro, 'Pro'),
        (veteran, 'Vetran'),
        (master, 'Master'),
        (god, 'God'),
    ]



    owner = models.ForeignKey(
        User, related_name='owner', on_delete=models.CASCADE
    )
    profile = models.ForeignKey(
        Profile, related_name='profile', on_delete=models.CASCADE
    )
    game = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    looking_for_friends = models.CharField(
        'Looking For Friends', blank=True, max_length=20,
        choices=looking_for_friends_choice
    )
    experience = models.CharField(
        'Experience Level', blank=True, max_length=20,
        choices=experience_level
    )
