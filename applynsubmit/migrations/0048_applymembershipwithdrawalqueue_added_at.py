# Generated by Django 3.0.6 on 2022-02-20 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applynsubmit', '0047_auto_20220220_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='applymembershipwithdrawalqueue',
            name='added_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
