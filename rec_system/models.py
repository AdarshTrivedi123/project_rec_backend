from django.db import models
from django.contrib.auth.models import User

class UserProfileData(models.Model):
    
    user = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)

    branch=models.CharField(null=True)
    academic_year=models.CharField(null=True)
    interest_field = models.CharField(max_length=100)  
    interest_domain = models.CharField(max_length=100)
    programming_language = models.CharField(max_length=100)
    frameworks = models.CharField(max_length=100)
    cloud_and_database = models.CharField(max_length=100)
    projects = models.TextField()
    achievements_and_awards = models.TextField()

    def __str__(self):
        return f"{self.user.username} - Profile Data"

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    skills = models.TextField()
    index = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.title}"
