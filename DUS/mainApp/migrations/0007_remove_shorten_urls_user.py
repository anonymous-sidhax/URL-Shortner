# Generated by Django 3.1.1 on 2020-10-18 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_auto_20201018_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorten_urls',
            name='user',
        ),
    ]
