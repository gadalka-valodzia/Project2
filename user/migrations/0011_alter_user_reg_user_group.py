# Generated by Django 4.1.5 on 2023-02-13 06:48

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_alter_user_reg_user_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_reg',
            name='user_group',
            field=models.CharField(default=django.contrib.auth.models.User, editable=False, max_length=40, null=True),
        ),
    ]
