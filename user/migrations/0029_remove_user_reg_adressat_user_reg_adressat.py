# Generated by Django 4.1.5 on 2023-02-26 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_operators', '0001_initial'),
        ('user', '0028_alter_user_reg_data_vidachi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_reg',
            name='adressat',
        ),
        migrations.AddField(
            model_name='user_reg',
            name='adressat',
            field=models.ManyToManyField(null=True, to='list_operators.operators', verbose_name='Адрессат'),
        ),
    ]
