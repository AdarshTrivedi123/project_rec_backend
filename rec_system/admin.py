from django.contrib import admin
from .models import UserProfileData, Bookmark

@admin.register(UserProfileData)
class UserProfileDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'branch', 'academic_year', 'interest_field', 'interest_domain', 'programming_language', 'frameworks', 'cloud_and_database')

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'skills', 'index')  
    search_fields = ('user__username', 'title', 'skills')  
    list_filter = ('user',)  

