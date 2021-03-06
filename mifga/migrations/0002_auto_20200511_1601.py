# Generated by Django 3.0.5 on 2020-05-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mifga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mifga',
            name='comment',
            field=models.TextField(default='None'),
        ),
        migrations.AddField(
            model_name='mifga',
            name='status',
            field=models.CharField(choices=[('open', 'OPEN'), ('in progress', 'IN PROGRESS'), ('closed', 'CLOSED')], default='open', max_length=255),
        ),
        migrations.AlterField(
            model_name='mifga',
            name='letter',
            field=models.CharField(default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='mifga',
            name='neighborhood',
            field=models.CharField(default='0', max_length=25),
        ),
        migrations.AlterField(
            model_name='mifga',
            name='street',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='mifga',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
