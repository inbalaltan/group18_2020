# Generated by Django 3.0.5 on 2020-05-30 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mifga', '0014_auto_20200530_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mifga',
            name='subscribed_issues',
        ),
    ]
