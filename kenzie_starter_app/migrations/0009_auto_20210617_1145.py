# Generated by Django 3.1 on 2021-06-17 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kenzie_starter_app', '0008_auto_20210617_1143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={},
        ),
        migrations.RemoveIndex(
            model_name='project',
            name='kenzie_star_name_499018_idx',
        ),
    ]
