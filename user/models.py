import requests
from django.db import models
from django.contrib.auth.models import Group, User
from transliterate import translit
from django.contrib.contenttypes.models import ContentType
from list_actions.models import Actions
from list_operators.models import Operators
from list_prichini.models import Prichini
from transliterate.discover import autodiscover
from transliterate import get_available_language_codes, translit
from transliterate.base import TranslitLanguagePack, registry
from django.contrib.auth import get_user_model

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

    NSP = models.CharField(max_length=40, null=True)  # ФИО сотрудника
    password = models.CharField(max_length=40, null=True)  # Пароль
    adressat = models.ForeignKey(Operators, on_delete=models.CASCADE, null=True)  # Адрессат
    action_id = models.ForeignKey(Actions, on_delete=models.CASCADE, null=True)
    prichina_id = models.ForeignKey(Prichini, on_delete=models.CASCADE, null=True)
    login = models.CharField(max_length=40, null=True, blank=True, editable=False)

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
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.NSP}'
