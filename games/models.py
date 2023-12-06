from django.db import models
from posts.models import Post
from django.contrib.auth.models import User

class Games(models.Model):
    """
    Games model category that links to the post model
    """
    cod = 'Call Of Duty'
    apex = 'Apex Legends'
    spiderman = 'SpiderMan'
    fifa = 'Fifa'
    zelda = 'Zelda'
    sbros = 'Smash Bros'
    pubg = 'PUBG'
    starfield = 'Starfield'


    games = [
        (cod, 'Call Of Duty'),
        (apex, 'Apex Legends'),
        (spiderman, 'SpiderMan'),
        (fifa, 'Fifa'),
        (zelda, 'Zelda'),
        (sbros, 'Smash Bros'),
        (pubg, 'PUBG'),
        (starfield, 'Starfield')
    ]

    owner = models.ForeignKey(
        User, related_name='owner', on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post, related_name='games', on_delete=models.CASCADE
    )
    game_choice = models.CharField(
        'Preferred Platform', max_length=20, blank=True, choices=games
    )