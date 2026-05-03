from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# This registers the User model with the default UserAdmin settings
admin.site.register(User, UserAdmin)