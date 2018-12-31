from django.contrib import admin

from dialogs.models import Thread, Message

admin.site.register(Thread)
admin.site.register(Message)