# Generated by Django 4.0.6 on 2022-09-13 17:36

import Feeds.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feeds', '0004_alter_posts_caption_alter_posts_pictures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='pictures',
            field=models.ImageField(blank=True, null=True, upload_to=Feeds.models.user_directory_path, verbose_name='Picture'),
        ),
    ]
