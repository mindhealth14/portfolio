# Generated by Django 4.2.7 on 2023-11-21 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myport', '0004_rename_category_project_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image_url',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]
