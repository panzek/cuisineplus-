# Generated by Django 4.1.2 on 2022-10-17 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_remove_cuisine_likes_remove_cuisine_restaurants_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='cuisines',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='price',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='review',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='time',
        ),
    ]
