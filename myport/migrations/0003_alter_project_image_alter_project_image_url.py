# Generated by Django 4.2.7 on 2023-11-20 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myport', '0002_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='projects/images'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
