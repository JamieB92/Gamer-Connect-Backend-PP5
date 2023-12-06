from rest_framework import serializers
from games.models import Games

class GamesSerializer(serializers.ModelSerializer):
    """
    Serializer for the Games model
    """
    post_in_game = serializers.ReadOnlyField(source='game_choice.post')

    class Meta:
        model = Games
        fields = ['id', 'game_choice', 'post_in_game', 'post']