# Generated by Django 3.1.2 on 2020-10-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_contactusmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactusmodel',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
