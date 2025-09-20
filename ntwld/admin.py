from django.contrib import admin
from .models import Client, Content, Like, FollowersCount, Bookmarks

# Register your models here.

admin.site.register(Client)
admin.site.register(Content)
admin.site.register(Like)
admin.site.register(FollowersCount)
admin.site.register(Bookmarks)
#admin.site.register(Comment)