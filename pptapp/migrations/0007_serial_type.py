# Generated by Django 3.2.4 on 2023-04-29 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pptapp', '0006_deletehistory_movehistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='serial',
            name='type',
            field=models.IntegerField(default=1),
        ),
    ]
