# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Articles(models.Model):
    text = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articles'


class Events(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    place_city = models.CharField(max_length=50, blank=True, null=True)
    place_country = models.CharField(max_length=50, blank=True, null=True)
    text = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class News(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    text = models.CharField(max_length=500, blank=True, null=True)
    img_path = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class Reviews(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    text = models.CharField(max_length=500, blank=True, null=True)
    img_path = models.ImageField(upload_to="upload/", blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviews'
