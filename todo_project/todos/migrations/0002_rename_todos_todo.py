# Generated by Django 4.2.3 on 2023-07-13 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todos',
            new_name='Todo',
        ),
    ]
