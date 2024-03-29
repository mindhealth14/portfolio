# Generated by Django 4.2.7 on 2024-01-06 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240)),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=240)),
                ('image', models.ImageField(blank=True, upload_to='projects/images')),
                ('embed_code', models.CharField(blank=True, max_length=550)),
                ('github', models.URLField(blank=True, max_length=500)),
                ('date', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='tutorial.category')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name'], name='tutorial_ca_name_66111b_idx'),
        ),
        migrations.AddIndex(
            model_name='course',
            index=models.Index(fields=['id', 'slug'], name='tutorial_co_id_b92a5d_idx'),
        ),
        migrations.AddIndex(
            model_name='course',
            index=models.Index(fields=['title'], name='tutorial_co_title_227643_idx'),
        ),
        migrations.AddIndex(
            model_name='course',
            index=models.Index(fields=['-date'], name='tutorial_co_date_490ad9_idx'),
        ),
    ]
