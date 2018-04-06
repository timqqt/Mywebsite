from django.contrib import admin
from django_web.models import BlogsPost


# Register your models here.
class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'timestamp']


admin.site.register(BlogsPost, BlogsPostAdmin)
# Register your models here.
