from django.contrib import admin
from main.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    def _username(self, obj):
        return obj.user.username
    def _email(self, obj):
        return obj.user.email
    def _first_name(self, obj):
        return obj.user.first_name
    def _last_name(self, obj):
        return obj.user.last_name
    list_display = ('user', '_username', '_email', '_first_name', '_last_name')
admin.site.register(UserProfile, UserProfileAdmin)
