# Generated by Django 5.0.3 on 2024-03-06 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_rename_car_cars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='cars',
            name='list_date',
        ),
    ]