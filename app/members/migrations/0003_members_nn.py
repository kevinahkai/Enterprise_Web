# Generated by Django 4.0.6 on 2022-08-08 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_remove_members_account_remove_members_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='nn',
            field=models.CharField(default='1', max_length=255),
        ),
    ]
