# Generated by Django 4.0.6 on 2022-08-22 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announce', '0005_news_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
