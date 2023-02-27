from xml.dom.minidom import Document

from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from jedi.inference.value import instance
from .forms import *
from .models import *
# from docx import newdocument


@admin.action(description='Выгрузка в Excel')
def vigruzka_xlm(modeladmin, request, queryset):
    response = HttpResponse(content_type='application/ms-excel')

    file_name = 'File.xlsx'  # Имя файла

    response['Content-Disposition'] = f'attachment; filename={escape_uri_path(file_name)}'

    workbook = openpyxl.Workbook()  # Создаем новый excel файл
    worksheet = workbook.active  # Получаем активный лист

    # Получаем данные из модели
    data = User_reg.objects.all().values_list('id', 'NSP', 'group_user', 'login', 'action_id__name_action')
    # Добавляем заголовки
    headers = ['id', 'ФИО', 'Группа', 'Логин', 'Действие']
    worksheet.append(headers)

    # Добавляем данные
    for row in data:
        worksheet.append(row)

    # Сохраняем файл и записываем его в response
    workbook.save(response)
    return response

@admin.action(description='Выгрузка в Word')
def create_word_doc(model):
    # Создание нового документа Word
    doc = Document()

    # Добавление заголовка
    doc.add_heading(model._meta.verbose_name_plural.title(), level=1)

    # Добавление данных в таблицу
    table = doc.add_table(rows=1, cols=len(model._meta.fields))
    header_cells = table.rows[0].cells
    for i, field in enumerate(model._meta.fields):
        header_cells[i].text = field.verbose_name.title()

    for obj in model.objects.all():
        row_cells = table.add_row().cells
        for i, field in enumerate(model._meta.fields):
            row_cells[i].text = str(getattr(obj, field.name))

    # Сохранение файла
    doc.save(f'{model._meta.verbose_name_plural}.docx')

@admin.register(User_reg)
class UserAdmin(admin.ModelAdmin):

    def save_model(self, request, User_reg, form, change):
        User_reg.group_user = request.user.groups.get().name
        super().save_model(request, User_reg, form, change)

    # def get_actions(self, request): разграничение прав для функций
    #     actions = super(UserAdmin, self).get_actions(request)
    #     if request.user.groups.get().name !='Минск':
    #         if 'vigruzka' in actions:
    #             del actions['vigruzka']
    #     return actions
    form = User_regForm

    readonly_fields = ['data_okonchaniya', 'login', 'group_user']
    list_display = ['NSP', 'login', 'password', 'get_adressats', 'group_user', 'action_id', 'prichina_id',
                    'data_vidachi',
                    'data_okonchaniya']
    ordering = ['NSP']
    list_per_page = 10
    search_fields = ['NSP']
    list_filter = ['NSP']
    actions = [vigruzka_xlm,create_word_doc]
