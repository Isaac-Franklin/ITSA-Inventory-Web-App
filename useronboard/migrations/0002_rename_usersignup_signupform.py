# Generated by Django 4.1.5 on 2023-01-12 13:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('useronboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserSignup',
            new_name='SignupForm',
        ),
    ]
