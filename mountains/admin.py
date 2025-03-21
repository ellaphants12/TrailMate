from django.contrib import admin
from .models import Mountain, Trail, Review

@admin.register(Mountain)
class MountainAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'elevation', 'difficulty')
    list_filter = ('difficulty', 'location')
    search_fields = ('name', 'location', 'description')

@admin.register(Trail)
class TrailAdmin(admin.ModelAdmin):
    list_display = ('name', 'mountain', 'length', 'difficulty', 'estimated_time')
    list_filter = ('difficulty', 'mountain')
    search_fields = ('name', 'description')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('mountain', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('comment', 'user__username', 'mountain__name')
