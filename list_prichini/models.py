from django.db import models

# Create your models here.
class Prichini(models.Model):
    class Meta:
        verbose_name = 'Причина'
        verbose_name_plural = 'Причины'
    name_prichina = models.CharField(max_length=40,verbose_name='Название')  # название причины