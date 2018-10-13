# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLoginHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ipAddress', models.GenericIPAddressField(null=True, blank=True)),
                ('macAddress', models.CharField(max_length=50, null=True, blank=True)),
                ('loginTime', models.DateTimeField(auto_now=True)),
                ('logoutTime', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email')),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=100, null=True, blank=True)),
                ('mobile', models.CharField(max_length=50, db_index=True)),
                ('ipAddress', models.GenericIPAddressField(null=True, blank=True)),
                ('macAddress', models.CharField(max_length=50, null=True, blank=True)),
                ('verificationCode', models.CharField(max_length=100, null=True, blank=True)),
                ('isEmailVerified', models.BooleanField(default=False)),
                ('verifiedOn', models.DateTimeField(null=True, blank=True)),
                ('otpSent', models.CharField(max_length=100, null=True, blank=True)),
                ('isOTPVerified', models.BooleanField(default=False)),
                ('otpVerifiedOn', models.DateTimeField(null=True, blank=True)),
                ('isPassChanged', models.BooleanField(default=False)),
                ('createdOn', models.DateTimeField(auto_now=True)),
                ('userType', models.CharField(default=b'A', max_length=2)),
                ('is_admin', models.BooleanField(default=False)),
                ('isActive', models.BooleanField(default=True)),
                ('activatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('isAgree', models.BooleanField(default=True)),
                ('isDeleted', models.BooleanField(default=False)),
                ('updatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('activatedBy', models.ForeignKey(related_name='activatedByUser', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='userloginhistory',
            name='userId',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
