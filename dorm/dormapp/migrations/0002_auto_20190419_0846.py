# Generated by Django 2.1.5 on 2019-04-19 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dormapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='IPadd',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='record',
            name='IPdelete',
            field=models.CharField(default='', max_length=30),
        ),
    ]
