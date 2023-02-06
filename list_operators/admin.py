from django.contrib import admin


from .models import *

# Register your models here.
@admin.register(Operators)
class OperatorsAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    list_per_page = 10
    search_fields = ['name']
    list_filter = ['name']