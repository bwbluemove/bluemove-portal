# Generated by Django 3.0.6 on 2021-07-10 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applynsubmit', '0029_auto_20210710_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applymembership',
            name='pf',
            field=models.CharField(blank=True, choices=[('미결정', '미결정'), ('선발', '선발'), ('미선발', '미선발')], default='미결정', max_length=5, null=True),
        ),
    ]