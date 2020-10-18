# Generated by Django 3.1.1 on 2020-10-18 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainApp', '0007_remove_shorten_urls_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorten_urls',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
