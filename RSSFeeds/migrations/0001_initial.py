# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField()),
                ('url', models.URLField()),
                ('author', models.CharField(max_length=200)),
                ('img_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Feeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='feeditems',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSSFeeds.Feeds'),
        ),
    ]
