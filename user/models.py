from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        verbose_name = 'Линые данные'
        verbose_name_plural = 'Личные данные'
    NSP = models.CharField(max_length=40)  # имя сотрудника
    self_phone_number = models.IntegerField(blank=True)  # номер мобильного телефона сотрудника
    home_phone_number = models.IntegerField(blank=True)  # номер городского телефона сотрудника
    passport_number = models.IntegerField()  # номер паспорта
