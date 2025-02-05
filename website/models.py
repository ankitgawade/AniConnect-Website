# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AniconnectAniDesc(models.Model):
    anime_id = models.IntegerField(primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    synopsis = models.TextField(db_column='Synopsis', blank=True, null=True)  # Field name made lowercase.
    image_url = models.TextField(db_column='Image_Url', blank=True, null=True)  # Field name made lowercase.
    genres = models.TextField(db_column='Genres', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aniconnect_ani_desc'
