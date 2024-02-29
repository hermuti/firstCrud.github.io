# Generated by Django 5.0.1 on 2024-02-29 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=255)),
                ('date_and_time', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('organizer_details', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('registration_id', models.AutoField(primary_key=True, serialize=False)),
                ('attendee_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_register.event')),
            ],
        ),
    ]