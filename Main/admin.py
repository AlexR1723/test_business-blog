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