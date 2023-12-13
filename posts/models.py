from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video


class Post(models.Model):
    """
    Post model related to the user.
    User can upload images and videos in a
    post and will be linked to the users account
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    post_header = models.CharField(max_length=255)
    caption = models.TextField(blank=True)
    upload_clip = models.FileField(
        upload_to='videos/', blank=True,
        storage=VideoMediaCloudinaryStorage(), validators=[validate_video])
    upload_image = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.post_header}'
