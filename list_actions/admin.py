from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
@admin.register(Actions)
class ActionsAdmin(admin.ModelAdmin):
    list_display = ['name_action']
    ordering = ['name_action']
    list_per_page = 10
    search_fields = ['name_action']
    list_filter = ['name_action']