# Generated by Django 3.1.2 on 2023-06-06 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carritocliente',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='carritocliente',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='carritoproducto',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='carritoproducto',
            name='updated_at',
        ),
    ]
