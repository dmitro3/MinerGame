# Generated by Django 5.0.6 on 2024-07-31 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_telegramuser_enery_lvl_telegramuser_refresh_energy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='video_lvl',
            field=models.IntegerField(default=1),
        ),
    ]
