from django.contrib import admin
from .models import Profile, Guide

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'is_guide')
    list_filter = ('is_guide', 'location')
    search_fields = ('user__username', 'bio', 'location')

@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ('user', 'experience_years', 'specialization', 'hourly_rate')
    list_filter = ('experience_years', 'specialization')
    search_fields = ('user__username', 'specialization', 'certification')
