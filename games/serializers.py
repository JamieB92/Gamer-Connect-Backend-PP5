from rest_framework import serializers
from games.models import Games

class GamesSerializer(serializers.ModelSerializer):
    """
    Serializer for the Games model
    """
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Games
        fields = ['id', 'is_owner', 'profile_id', 'game', 'content',
        'looking_for_friends', 'experience', 'profile'
       ]


class GamesDetailSerializer(serializers.ModelSerializer):

    profile = serializers.ReadOnlyField(source='profile.id')