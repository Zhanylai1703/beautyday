from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.otzyv.models import Review


@admin.register(Review)
class UserAdmin(admin.ModelAdmin):
    list_display = (
            'id',
            'name',
            'description',
            'quality',
            'atmosphere',
        )