# Generated by Django 3.2.23 on 2023-12-12 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_auto_20231212_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='experience',
            field=models.CharField(blank=True, choices=[('Noob', 'Noob'), ('Casual', 'Casual'), ('Pro', 'Pro'), ('Veteran', 'Veteran'), ('Master', 'Master'), ('God', 'God')], max_length=20, verbose_name='Experience Level'),
        ),
        migrations.AlterField(
            model_name='games',
            name='friends',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, verbose_name='Friends'),
        ),
        migrations.AlterField(
            model_name='games',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
