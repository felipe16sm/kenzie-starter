# Generated by Django 3.1 on 2021-06-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kenzie_starter_app', '0007_auto_20210617_1140'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['name', 'state']},
        ),
        migrations.AddIndex(
            model_name='project',
            index=models.Index(fields=['name', 'state'], name='kenzie_star_name_499018_idx'),
        ),
    ]