# Generated by Django 3.1.4 on 2020-12-09 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0002_auto_20201208_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='slug',
        ),
    ]