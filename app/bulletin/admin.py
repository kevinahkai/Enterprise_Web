#公告
from django.contrib import admin

from bulletin.models import Topic, Entry
admin.site.register(Topic)
admin.site.register(Entry)