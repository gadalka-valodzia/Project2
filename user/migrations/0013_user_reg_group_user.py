# Generated by Django 4.1.5 on 2023-02-13 08:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0012_remove_user_reg_user_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_reg',
            name='group_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
