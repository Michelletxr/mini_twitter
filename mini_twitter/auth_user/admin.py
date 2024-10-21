from django.contrib import admin

from auth_user.models import UserAccount

# Register your models here.

@admin.register(UserAccount)
class UserAcountAdmin(admin.ModelAdmin):
    search_fields = ('username', 'email')
    ordering = ('first_name',)
    
