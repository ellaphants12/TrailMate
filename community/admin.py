from django.contrib import admin
from .models import Post, Comment, Message, Event, EventParticipant

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'mountain', 'created_at')
    list_filter = ('created_at', 'mountain')
    search_fields = ('title', 'content', 'user__username')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content', 'user__username', 'post__title')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    search_fields = ('content', 'sender__username', 'recipient__username')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'mountain', 'organizer', 'start_date', 'end_date')
    list_filter = ('start_date', 'mountain')
    search_fields = ('title', 'description', 'organizer__username')

@admin.register(EventParticipant)
class EventParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'registered_at')
    list_filter = ('registered_at', 'event')
    search_fields = ('user__username', 'event__title')
