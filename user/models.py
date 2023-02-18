import datetime

import requests
from dateutil.relativedelta import relativedelta
from django import forms
from django.db import models
from django.contrib.auth.models import Group, User
from django.forms import ModelForm
from transliterate import translit
from django.contrib.contenttypes.models import ContentType
from list_actions.models import Actions
from list_operators.models import Operators
from list_prichini.models import Prichini
from transliterate.discover import autodiscover
from transliterate import get_available_language_codes, translit
from transliterate.base import TranslitLanguagePack, registry
from django.contrib.auth import get_user_model
from project2 import settings

autodiscover()

class ExampleLanguagePack(TranslitLanguagePack):
    language_code = "example"
    language_name = "Example"
    mapping = (
        u"АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЫЭЮабвгдеёжзийклмнопрстуфхыэю ",
        u"ABVGDEEJZIIKLMNOPRSTUFHIEUabvgdeejziiklmnoprstufhieu_",

    )
    pre_processor_mapping = {
        u"я": u"ya",
        u"ь": u"'",
        u"ъ": u"'",
        u"ч": u"ch",
        u"ш": u"sh",
        u"щ": u"sch"

    }


registry.register(ExampleLanguagePack)

_requests = {}


class User_reg(models.Model):
    class Meta:
        verbose_name = 'Линые данные'
        verbose_name_plural = 'Личные данные'

    NSP = models.CharField(max_length=40, null=True,verbose_name='ФИО',help_text='Формат: Фамилия Имя Отчество. В случае отсутствия одного из пунктов указать любую букву вместо')  # ФИО сотрудника
    password = models.CharField(max_length=40, null=True, verbose_name='Пароль')  # Пароль
    adressat = models.ForeignKey(Operators, on_delete=models.CASCADE, null=True,verbose_name= 'Адрессат')
    action_id = models.ForeignKey(Actions, on_delete=models.CASCADE, null=True,verbose_name='Действие')
    prichina_id = models.ForeignKey(Prichini, on_delete=models.CASCADE, null=True,verbose_name='Причина')
    login = models.CharField(max_length=40, null=True, blank=True, editable=False,verbose_name='Логин') #Логин пользователя
    data_vidachi=models.DateField(null=True, blank=True,verbose_name='Дата выдачи пароля')
    data_okonchaniya = models.DateField(editable=False,null=True, blank=True,verbose_name='Дата окончания пароля')

    def data(self):
        return self.data_vidachi + relativedelta(months=10)

    def groups_g(self):
        a = User.objects.all()
        for b in a:
             if b.is_authenticated:
                 return b.groups.all().get().name
    def login_set(self):
        arg = u"{}_{[0]}{[0]}".format(*(translit(self.NSP.lower(), 'example')).split('_'))
        return arg

    def save(self, *args, **kwargs):
        self.login = self.login_set()
        self.data_okonchaniya=self.data()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.NSP}'

