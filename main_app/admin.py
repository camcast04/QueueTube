# queuetube/main_app/admin.py

from django.contrib import admin
from .models import Playlist, Video
# Register your models here.
admin.site.register(Playlist)
admin.site.register(Video)
