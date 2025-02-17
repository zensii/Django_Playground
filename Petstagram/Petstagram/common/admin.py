from django.contrib import admin

from Petstagram.common.models import Comment, Like


# Register your models here.
@admin.register(Comment)
class LikeAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass