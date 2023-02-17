from django.contrib import admin
from jedi.inference.value import instance

from  .models import *

# Register your models here.
@admin.register(User_reg)
class UserAdmin(admin.ModelAdmin):
    list_display = ['NSP','login','password','adressat','action_id','prichina_id','groups_g']
    ordering = ['NSP']
    list_per_page = 10
    search_fields = ['NSP', 'self_phone_number', 'home_phone_number', 'passport_number']
    list_filter = ['NSP']

