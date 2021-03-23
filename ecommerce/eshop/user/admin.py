from django.contrib import admin
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import UserProfile


# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ['id', 'first_name', 'last_name', 'phone']

admin.site.register(UserProfile)
