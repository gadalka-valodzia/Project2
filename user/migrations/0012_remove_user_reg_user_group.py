# Generated by Django 4.1.5 on 2023-02-13 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_user_reg_user_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_reg',
            name='user_group',
        ),
    ]
