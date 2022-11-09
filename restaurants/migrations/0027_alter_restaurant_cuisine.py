# Generated by Django 4.1.2 on 2022-11-09 17:03

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0026_rename_restaurant_menu_restaurants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='cuisine',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'African'), (2, 'Chinese'), (3, 'Asian'), (4, 'Irish'), (5, 'Continental')], max_length=3, null=True),
        ),
    ]
