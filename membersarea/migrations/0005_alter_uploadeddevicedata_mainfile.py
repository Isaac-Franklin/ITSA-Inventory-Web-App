# Generated by Django 4.0.5 on 2023-02-02 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membersarea', '0004_uploadeddevicedata_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadeddevicedata',
            name='mainfile',
            field=models.FileField(null=True, upload_to='uploadedfiles/'),
        ),
    ]
