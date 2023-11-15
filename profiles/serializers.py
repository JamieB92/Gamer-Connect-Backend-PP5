from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_on', 'edited_on', 'name',
            'bio', 'profile_avatar', 'platform', 'platform_username',
        ]