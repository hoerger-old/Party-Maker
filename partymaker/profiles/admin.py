from django.contrib import admin
from profiles.models import UserFieldType, UserField

class UserFieldTypeAdmin(admin.ModelAdmin):
        pass
admin.site.register(UserFieldType, UserFieldTypeAdmin)

class UserFieldAdmin(admin.ModelAdmin):
    def _username(self, obj):
        return obj.user.username
    list_display=('name', 'content', '_username')

admin.site.register(UserField, UserFieldAdmin)

