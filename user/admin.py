from django.contrib import admin
from  .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['NSP', 'self_phone_number', 'home_phone_number', 'passport_number']
    ordering = ['NSP']
    list_per_page = 10
    search_fields = ['NSP', 'self_phone_number', 'home_phone_number', 'passport_number']
    list_filter = ['NSP']