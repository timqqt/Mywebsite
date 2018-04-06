from django.contrib import admin
from guestbook.models import Message


# Register your models here.
class MsgsPostAdmin(admin.ModelAdmin):
    list_display = ['username', 'title', 'content', 'publish']


admin.site.register(Message, MsgsPostAdmin)
# Register your models here.
