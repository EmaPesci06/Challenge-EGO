# Generated by Django 5.0.3 on 2024-03-06 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_remove_cars_is_published_remove_cars_list_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='mileage',
        ),
    ]
