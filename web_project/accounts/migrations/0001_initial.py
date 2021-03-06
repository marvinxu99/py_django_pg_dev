# Generated by Django 3.0.4 on 2020-03-29 06:50

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('name_first', models.CharField(default='John', max_length=128, verbose_name='Fist Name')),
                ('name_middle', models.CharField(blank=True, max_length=128, null=True, verbose_name='Middle Name')),
                ('name_last', models.CharField(default='Doe', max_length=128, verbose_name='Last Name')),
                ('name_full_formatted', models.CharField(default='John Doe, MD', max_length=128, verbose_name='Full Name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('active_status_cd', models.IntegerField(default=1, verbose_name='Active Status')),
                ('active_status_dt_tm', models.DateTimeField(auto_now_add=True, verbose_name='Active Status Date')),
                ('person_type_cd', models.IntegerField(default=1, verbose_name='User Type')),
                ('created_dt_tm', models.DateTimeField(blank=True, null=True, verbose_name='Date Created')),
                ('create_id', models.BigIntegerField(blank=True, null=True, verbose_name='Created by')),
                ('updated_dt_tm', models.DateTimeField(blank=True, null=True, verbose_name='Date Updated')),
                ('update_id', models.BigIntegerField(blank=True, null=True, verbose_name='Updated by')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prsnl',
            fields=[
                ('prsnl_id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
                ('active_status_cd', models.IntegerField(default=1, verbose_name='Ative Status')),
                ('name_first', models.CharField(blank=True, max_length=128, verbose_name='Fist Name')),
                ('name_middle', models.CharField(blank=True, max_length=128, verbose_name='Middle Name')),
                ('name_last', models.CharField(blank=True, max_length=128, verbose_name='Last Name')),
                ('name_full_formatted', models.CharField(blank=True, max_length=128, verbose_name='Full Name')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prsnl_Alias',
            fields=[
                ('prsnl_alias_id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=1, verbose_name='Active')),
                ('active_status_cd', models.IntegerField(default=1, verbose_name='Ative Status')),
                ('alias', models.CharField(default='abc', max_length=200, verbose_name='Alias')),
                ('alias_expiry_dt_tm', models.DateTimeField(blank=True, null=True, verbose_name='Alias Expiry Date')),
                ('alias_pool_cd', models.IntegerField(default=1, verbose_name='Alias Type')),
                ('prsnl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Prsnl')),
            ],
        ),
        migrations.CreateModel(
            name='Person_Alias',
            fields=[
                ('person_alias_id', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('active_ind', models.BooleanField(verbose_name='Active')),
                ('active_status_cd', models.IntegerField(verbose_name='Ative Status')),
                ('alias', models.CharField(max_length=200, verbose_name='Alias')),
                ('alias_expiry_dt_tm', models.DateTimeField(verbose_name='Alias Expiry Date')),
                ('alias_pool_cd', models.IntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.Person')),
            ],
        ),
    ]
