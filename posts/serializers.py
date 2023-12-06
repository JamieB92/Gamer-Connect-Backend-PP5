from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from games.models import Games


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_avatar = serializers.ReadOnlyField(source='owner.profile.profile_avatar.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    games_id = serializers.SerializerMethodField()


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_games_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            games = Games.objects.filter(
                owner=user, post=obj
            ).first()
            return games.id if games else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_avatar', 'created_at', 'edited_on',
            'post_header', 'caption', 'upload_clip', 'upload_image',
            'like_id', 'likes_count', 'comments_count', 'games_id',
        ]