# Generated by Django 3.0.6 on 2022-05-19 01:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Applymembershipwithdrawal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.CharField(max_length=4)),
                ('phone_last', models.CharField(max_length=4)),
                ('email_host', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '인증 코드',
                'verbose_name_plural': '인증 코드(들)',
            },
        ),
        migrations.CreateModel(
            name='ApplymembershipwithdrawalQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('period', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('activities', models.CharField(max_length=300)),
                ('data_boolean', models.BooleanField(default=False)),
                ('reason', models.CharField(max_length=50)),
                ('row_idx', models.CharField(max_length=10)),
                ('slack_ts', models.CharField(max_length=100)),
                ('added_at', models.DateTimeField(blank=True, null=True)),
                ('will_be_deleted_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': '탈퇴 신청자',
                'verbose_name_plural': '탈퇴 신청자(들)',
            },
        ),
        migrations.CreateModel(
            name='ApplymembershipNoti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wanted_id', models.CharField(blank=True, max_length=36, null=True)),
                ('wanted_title', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('passed_content', models.TextField(blank=True, max_length=510, null=True)),
                ('failed_content', models.TextField(blank=True, max_length=510, null=True)),
                ('sent', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('will_be_deleted_on', models.DateTimeField(blank=True, null=True)),
                ('saved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '통보 메일',
                'verbose_name_plural': '통보 메일(들)',
            },
        ),
        migrations.CreateModel(
            name='Applymembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wanted_id', models.CharField(blank=True, max_length=36, null=True)),
                ('wanted_title', models.CharField(blank=True, max_length=50, null=True)),
                ('self_intro', models.TextField(blank=True, max_length=260, null=True)),
                ('self_intro_len', models.IntegerField(blank=True, default=0, null=True)),
                ('reason', models.TextField(blank=True, max_length=260, null=True)),
                ('reason_len', models.IntegerField(blank=True, default=0, null=True)),
                ('plan', models.TextField(blank=True, max_length=260, null=True)),
                ('plan_len', models.IntegerField(blank=True, default=0, null=True)),
                ('tracking', models.CharField(blank=True, max_length=20, null=True)),
                ('tracking_reference', models.CharField(blank=True, max_length=10, null=True)),
                ('tracking_etc', models.CharField(blank=True, max_length=100, null=True)),
                ('portfolio', models.CharField(blank=True, max_length=100, null=True)),
                ('last_saved', models.BooleanField(default=False)),
                ('received', models.BooleanField(default=False)),
                ('pf', models.CharField(blank=True, choices=[('미선발', '미선발'), ('선발', '선발'), ('미결정', '미결정')], default='미결정', max_length=5, null=True)),
                ('notified', models.BooleanField(default=False)),
                ('joined', models.BooleanField(default=False)),
                ('received_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('will_be_deleted_on', models.DateTimeField(blank=True, null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '지원서',
                'verbose_name_plural': '지원서(들)',
            },
        ),
    ]
