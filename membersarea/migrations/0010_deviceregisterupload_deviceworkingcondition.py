# Generated by Django 4.0.5 on 2023-02-04 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membersarea', '0009_deviceregisterupload_deviceuserdateofresumption_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceregisterupload',
            name='deviceworkingcondition',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]