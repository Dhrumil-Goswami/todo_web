# Generated by Django 5.0.3 on 2024-03-10 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tasks',
            new_name='Task',
        ),
    ]
