# Generated by Django 5.1.1 on 2024-09-27 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_teams_dateadded_alter_teams_instagramuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='description',
            field=models.CharField(blank=True, default='Description here', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='dateAdded',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 27, 13, 42, 48, 691218)),
        ),
    ]
