# Generated by Django 5.0.4 on 2024-05-04 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aniconnect', '0007_userprofile_background_image_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='background_image_url',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image_url',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]