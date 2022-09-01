from re import T
from django.contrib import admin
from .models import Posts,Likes,Follow,Stream

admin.site.register(Posts)
admin.site.register(Likes)
admin.site.register(Follow)
admin.site.register(Stream)


# Register your models here.
