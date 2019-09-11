# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Articles(models.Model):
    text = models.CharField(max_length=500, blank=True, null=True, verbose_name='Текст')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Заголовок')

    class Meta:
        managed = False
        db_table = 'articles'
        verbose_name_plural = 'Статьи'


class Events(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Заголовок')
    date_start = models.DateField(blank=True, null=True, verbose_name='Дата начала')
    date_end = models.DateField(blank=True, null=True, verbose_name='Дата конца')
    place_city = models.CharField(max_length=50, blank=True, null=True, verbose_name='Город')
    place_country = models.CharField(max_length=50, blank=True, null=True, verbose_name='Страна')
    text = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Текст')

    class Meta:
        managed = False
        db_table = 'events'
        # verbose_name = 'Уже скоро'
        verbose_name_plural = 'Уже скоро'


class News(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Заголовок')
    text = models.CharField(max_length=500, blank=True, null=True, verbose_name='Текст')
    img_path = models.ImageField(upload_to="upload/", blank=True, null=True, verbose_name='Изображение')

    class Meta:
        managed = False
        db_table = 'news'
        verbose_name_plural = 'Новости'


class Reviews(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Имя')
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name='Город')
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name='Страна')
    text = models.CharField(max_length=500, blank=True, null=True, verbose_name='Текст')
    position = models.CharField(max_length=100, blank=True, null=True, verbose_name='Должность')

    class Meta:
        managed = False
        db_table = 'reviews'
        verbose_name_plural = 'Отзывы'
