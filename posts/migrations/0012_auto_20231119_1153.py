# Generated by Django 3.2.23 on 2023-11-19 11:53

import cloudinary_storage.storage
import cloudinary_storage.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_alter_post_upload_clip'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upload_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='upload_clip',
            field=models.ImageField(blank=True, storage=cloudinary_storage.storage.VideoMediaCloudinaryStorage(), upload_to='videos/', validators=[cloudinary_storage.validators.validate_video]),
        ),
    ]