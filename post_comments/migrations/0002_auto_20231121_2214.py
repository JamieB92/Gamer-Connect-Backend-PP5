# Generated by Django 3.2.23 on 2023-11-21 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='commented_at',
            new_name='created_at',
        ),
    ]