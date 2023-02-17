# Generated by Django 4.0.5 on 2023-02-04 20:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('membersarea', '0008_deviceregisterupload_devicedepreciationrate'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceregisterupload',
            name='deviceuserdateofresumption',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='deviceregisterupload',
            name='deviceuseremail',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='deviceregisterupload',
            name='deviceuserphonenumber',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='StaffDataSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceuser', models.CharField(blank=True, max_length=200, null=True)),
                ('deviceuserphonenumber', models.CharField(blank=True, max_length=200, null=True)),
                ('deviceuseremail', models.CharField(blank=True, max_length=200, null=True)),
                ('deviceuserdateofresumption', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-edited_at', '-created_at'],
            },
        ),
    ]