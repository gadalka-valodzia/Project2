from django.db import models

# Create your models here.
class Operators(models.Model):
    class Meta:
        verbose_name = 'Оператор связи'
        verbose_name_plural = 'Операторы связи'
    name = models.CharField(max_length=40,verbose_name='Название')  # имя сотрудника

# Create your models here.
