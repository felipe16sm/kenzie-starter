# Generated by Django 3.1 on 2021-06-17 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kenzie_starter_app', '0002_auto_20210617_0502'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['name', 'state']},
        ),
        migrations.RemoveIndex(
            model_name='project',
            name='kenzie_star_name_4b0ea2_idx',
        ),
        migrations.AddIndex(
            model_name='project',
            index=models.Index(fields=['name', 'state'], name='kenzie_star_name_499018_idx'),
        ),
    ]
