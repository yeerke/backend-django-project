from django.contrib import admin

from recruting.message.models import Chat


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_mes', 'to_mes', 'mess', 'date')
    