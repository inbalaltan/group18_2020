# Generated by Django 3.0.5 on 2020-05-30 14:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mifga', '0015_remove_mifga_subscribed_issues'),
    ]

    operations = [
        migrations.AddField(
            model_name='mifga',
            name='subscribed_issues',
            field=models.ManyToManyField(default='1', related_name='_mifga_subscribed_issues_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
