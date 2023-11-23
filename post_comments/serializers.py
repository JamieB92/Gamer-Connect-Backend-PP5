from django.contrib.humanize.templatetags.humanize import naturaltime
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
    created_at = serializers.SerializerMethodField()
    edited_on = serializers.SerializerMethodField()


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_edited_on(self, obj):
        return naturaltime(obj.edited_on)

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_avatar',
            'post', 'created_at', 'edited_on', 'comment'
        ]

class PostCommentDetailSerializer(PostCommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    post = serializers.ReadOnlyField(source='post.id')