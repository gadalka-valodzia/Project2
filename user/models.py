
from django.db import models
from django.contrib.auth.models import Group, User
from list_actions.models import Actions
from list_operators.models import Operators
from list_prichini.models import Prichini



class User(models.Model):
    class Meta:
        verbose_name = 'Линые данные'
        verbose_name_plural = 'Личные данные'
    NSP = models.CharField(max_length=40,null=True)  # ФИО сотрудника
    login = models.CharField(max_length=40,null=True) # Логин сотрудника
    password = models.CharField(max_length=40, null=True) #Пароль
    adressat = models.ForeignKey(Operators,on_delete=models.CASCADE,null=True) #Адрессат
    action_id = models.ForeignKey(Actions,on_delete=models.CASCADE,null=True)
    prichina_id=models.ForeignKey(Prichini,on_delete=models.CASCADE,null=True)
    group=models.ForeignKey(,on_delete=models.CASCADE,max_length=40,null=True)
    def __str__(self):
        return f'{self.NSP}'