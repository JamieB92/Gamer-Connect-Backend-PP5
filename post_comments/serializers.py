from rest_framework import serializers
from .models import Comment


class PostCommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the post_Comment model
    Adds extra fields when listing the comments on a post
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_avatar = serializers.ReadOnlyField(source='owner.profile.profile_avatar.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_avatar',
            'post', 'commented_at', 'edited_on', 'comment'
        ]