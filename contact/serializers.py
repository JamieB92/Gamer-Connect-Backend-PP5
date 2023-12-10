from rest_framework import serializers
from .models import Contact


class ContactFormSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contact model

    """
    owner = serializers.ReadOnlyField(source="owner.username")
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_avatar = serializers.ReadOnlyField(source="owner.profile.profile_avatar.url")


    class Meta:
        """
        List of the filed returning in the API
        """
        model = Contact
        fields = [
            "id",
            "owner",
            "subject",
            "content",
            "profile_id",
            "profile_avatar",
            "created_at",
            "updated_at",
        ]