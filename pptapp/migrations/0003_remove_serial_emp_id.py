# Generated by Django 3.1.3 on 2021-10-17 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pptapp', '0002_auto_20211017_0810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serial',
            name='emp_id',
        ),
    ]
