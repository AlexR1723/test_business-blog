from django.contrib import admin
from .models import *


class EventsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Events._meta.fields]

    class Meta:
        model = Events

admin.site.register(Events, EventsAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in News._meta.fields]

    class Meta:
        model = News

admin.site.register(News, NewsAdmin)


class ArticlesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Articles._meta.fields]

    class Meta:
        model = Articles

admin.site.register(Articles, ArticlesAdmin)


class ReviewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Reviews._meta.fields]

    class Meta:
        model = Reviews

admin.site.register(Reviews, ReviewsAdmin)