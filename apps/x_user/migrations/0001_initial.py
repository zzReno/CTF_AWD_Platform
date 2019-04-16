# Generated by Django 2.1.7 on 2019-04-16 09:48

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('x_team', '0001_initial'),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_name', models.CharField(blank=True, max_length=30, verbose_name='姓名')),
                ('user_password', models.CharField(blank=True, max_length=50, verbose_name='密码')),
                ('user_school', models.CharField(blank=True, max_length=30, null=True, verbose_name='学校')),
                ('user_major', models.CharField(blank=True, max_length=30, null=True, verbose_name='专业班级')),
                ('user_phone', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='手机')),
                ('user_number', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='学号')),
                ('user_email', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='邮箱')),
                ('user_image', models.ImageField(blank=True, upload_to='avatar/%Y/%m/%d', verbose_name='头像')),
                ('user_url', models.CharField(blank=True, max_length=36, null=True, verbose_name='个人网址')),
                ('user_gender', models.SmallIntegerField(choices=[(0, '男'), (1, '女'), (2, '未知')], default=2)),
                ('user_ip', models.CharField(blank=True, max_length=15, null=True, verbose_name='ip')),
                ('user_str', models.CharField(blank=True, max_length=36, verbose_name='随机字符串')),
                ('user_registertime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='注册时间')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
                ('user_team_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_team121', to='x_team.TeamProfile')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'UserProfile',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='user_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '登陆日志',
                'verbose_name_plural': '登陆日志',
                'db_table': 'User_Log',
            },
        ),
    ]
