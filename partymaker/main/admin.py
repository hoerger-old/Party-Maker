from django.contrib import admin
from main.models import UserProfile, UserFieldType, UserField, Vote

class UserProfileAdmin(admin.ModelAdmin):
        pass
admin.site.register(UserProfile, UserProfileAdmin)

class UserFieldTypeAdmin(admin.ModelAdmin):
        pass
admin.site.register(UserFieldType, UserFieldTypeAdmin)

class UserFieldAdmin(admin.ModelAdmin):
        pass
admin.site.register(UserField, UserFieldAdmin)

class VoteAdmin(admin.ModelAdmin):
        pass
admin.site.register(Vote, VoteAdmin)
