from django.contrib import admin
from profiles.models import UserFieldType, UserField

class UserFieldTypeAdmin(admin.ModelAdmin):
        pass
admin.site.register(UserFieldType, UserFieldTypeAdmin)

class UserFieldAdmin(admin.ModelAdmin):
        pass
admin.site.register(UserField, UserFieldAdmin)

