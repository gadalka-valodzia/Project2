from django.contrib import admin
from  .models import *

# Register your models here.
@admin.register(Prichini)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name_prichina']
    ordering = ['name_prichina']
    list_per_page = 10
    search_fields = ['name_prichina']
    list_filter = ['name_prichina']