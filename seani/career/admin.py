from django.contrib import admin

from .models import Career
# Register your models here.


@admin.register(Career)
class CarerrAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'level']
    ordering = ['short_name', 'level']
