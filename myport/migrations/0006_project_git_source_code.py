# Generated by Django 4.2.7 on 2023-11-21 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myport', '0005_alter_project_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='git_source_code',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
