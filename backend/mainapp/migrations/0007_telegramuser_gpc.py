# Generated by Django 5.0.6 on 2024-07-27 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_rename_gold_per_hour_telegramuser_gph'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='gpc',
            field=models.IntegerField(default=1),
        ),
    ]
