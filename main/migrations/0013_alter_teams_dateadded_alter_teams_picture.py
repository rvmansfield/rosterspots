# Generated by Django 5.1.1 on 2024-10-05 22:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_teams_dateadded_alter_teams_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='dateAdded',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 5, 18, 4, 49, 302697)),
        ),
        migrations.AlterField(
            model_name='teams',
            name='picture',
            field=models.ImageField(default='default.png', upload_to='static/images/teams'),
        ),
    ]