# Generated by Django 4.1.5 on 2023-02-13 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list_actions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0015_alter_user_reg_action_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_reg',
            name='action_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='list_actions.actions'),
        ),
        migrations.AlterField(
            model_name='user_reg',
            name='group_user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]