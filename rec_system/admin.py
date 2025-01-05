from django.contrib import admin
from .models import UserProfileData

@admin.register(UserProfileData)
class UserProfileDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'interest_field', 'interest_domain', 'programming_language', 'frameworks', 'cloud_and_database')

