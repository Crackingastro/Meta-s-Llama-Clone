# Generated by Django 4.2.6 on 2024-01-16 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='answer',
        ),
        migrations.DeleteModel(
            name='question',
        ),
    ]
