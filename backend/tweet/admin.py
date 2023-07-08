from django.contrib import admin

from tweet.models import Tweet, Comment, Media

admin.site.register(Tweet)
admin.site.register(Comment)
admin.site.register(Media)
