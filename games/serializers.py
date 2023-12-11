from rest_framework import serializers
from games.models import Games

class GamesSerializer(serializers.ModelSerializer):
    """
    Serializer for the Games model
    """
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')

    class Meta:
        model = Games
        fields = ['id', 'is_owner', 'profile_id', 'game', 'content',
        'looking_for_friends', 'experience'
       ]
