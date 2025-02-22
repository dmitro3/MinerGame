# Generated by Django 5.0.6 on 2024-08-05 17:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_telegramuser_friends_invited'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='daily_reward_claimed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='daily_reward_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='daily_reward_day',
            field=models.IntegerField(default=0),
        ),
    ]
