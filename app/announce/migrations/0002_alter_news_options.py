# Generated by Django 4.0.6 on 2022-08-17 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announce', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'permissions': [('can_read', 'Can read'), ('can_insert', 'Can add announce'), ('can_update', 'Can edit announce'), ('can_delete', 'Can delete announce')]},
        ),
    ]