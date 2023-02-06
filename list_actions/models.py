from django.db import models

# Create your models here.
class Actions(models.Model):
    class Meta:
        verbose_name = 'Действие'
        verbose_name_plural = 'Действия'
    name_action = models.CharField(max_length=40,verbose_name='Название')  # название действия