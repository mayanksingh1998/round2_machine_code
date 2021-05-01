# Generated by Django 3.2 on 2021-05-01 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, default=None, max_length=255, null=True)),
                ('phone', models.CharField(blank=True, db_index=True, default=None, max_length=25, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], db_index=True, default='active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_location', models.CharField(blank=True, db_index=True, default=None, max_length=255, null=True)),
                ('price', models.IntegerField(blank=True, db_index=True, default=None, max_length=255, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], db_index=True, default='active', max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='RideDriver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ride_sharing.driver')),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ride_sharing.ride')),
            ],
        ),
    ]