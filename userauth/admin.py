from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from userauth.models import CustomUser

# Register your models here.

class CustomUserInline(admin.StackedInline):
	model = CustomUser
	can_delete = False
	verbose_name = '其他信息'
	verbose_name_plural = '其他信息'

class UserAdmin(BaseUserAdmin):
	inlines = [CustomUserInline, ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
#admin.site.register(CustomUser)