# Generated by Django 3.2 on 2021-05-01 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride_sharing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='start_location',
            new_name='drop_location',
        ),
        migrations.AddField(
            model_name='ride',
            name='pickup_location',
            field=models.CharField(blank=True, db_index=True, default=None, max_length=255, null=True),
        ),
    ]
