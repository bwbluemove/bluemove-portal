# Generated by Django 3.0.6 on 2022-02-21 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applynsubmit', '0048_applymembershipwithdrawalqueue_added_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applymembership',
            name='pf',
            field=models.CharField(blank=True, choices=[('미선발', '미선발'), ('미결정', '미결정'), ('선발', '선발')], default='미결정', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='applymembershipwithdrawalqueue',
            name='reason',
            field=models.CharField(max_length=50),
        ),
    ]