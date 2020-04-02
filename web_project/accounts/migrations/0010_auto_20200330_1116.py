# Generated by Django 3.0.4 on 2020-03-30 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200330_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prsnl',
            name='colour_code',
            field=models.CharField(choices=[('red', 'Red'), ('blue', 'Blue'), ('orange', 'Orange'), ('green', 'Green')], default='green', help_text='The colour of their care team(not their skin colour)', max_length=6),
        ),
        migrations.AlterField(
            model_name='prsnl',
            name='user',
            field=models.OneToOneField(help_text='Each staff member must have a username which is used to login to the Winter Winn system', limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='username'),
        ),
    ]