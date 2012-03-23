from django.contrib import admin
from main.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
        pass
admin.site.register(UserProfile, UserProfileAdmin)
