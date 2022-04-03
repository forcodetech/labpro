# Generated by Django 3.0.7 on 2022-04-01 16:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='lab_task_summary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
                ('research_type', models.CharField(max_length=50)),
                ('equpments', models.CharField(max_length=255)),
                ('findings', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'verbose_name_plural': 'Laboratory Tasks',
            },
        ),
    ]
