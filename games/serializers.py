from rest_framework import serializers
from games.models import Games

class GamesSerializer(serializers.ModelSerializer):
    """
    Serializer for the Games model
    """
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_avatar = serializers.ReadOnlyField(
        source='owner.profile.profile_avatar.url'
        )
    platform = serializers.ReadOnlyField(
        source='owner.profile.platform'
        )
    platform_username = serializers.ReadOnlyField(
        source='owner.profile.platform_username'
        )

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Games
        fields = ['id', 'is_owner', 'profile_id', 'name', 'content',
        'friends', 'experience', 'profile_avatar',
        'platform', 'platform_username'
       ]
