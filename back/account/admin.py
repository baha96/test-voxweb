# -*- coding:utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from account import models


class UserInline(admin.StackedInline):
    model = models.UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


class UserAdministrator(UserAdmin):
    inlines = (UserInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdministrator)
