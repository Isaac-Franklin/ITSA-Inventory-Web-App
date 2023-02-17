# Generated by Django 4.0.5 on 2023-02-02 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membersarea', '0005_alter_uploadeddevicedata_mainfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deviceregisterupload',
            old_name='devicelocation',
            new_name='devicemultiplepacket',
        ),
        migrations.RenameField(
            model_name='deviceregisterupload',
            old_name='deviceprocessor',
            new_name='devicename',
        ),
        migrations.RenameField(
            model_name='deviceregisterupload',
            old_name='deviceserialnumber',
            new_name='deviceportnumber',
        ),
        migrations.RenameField(
            model_name='deviceregisterupload',
            old_name='devicetype',
            new_name='devicestatus',
        ),
        migrations.AddField(
            model_name='deviceregisterupload',
            name='deviceworkgroup',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='deviceregisterupload',
            name='index',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]