# Generated by Django 4.0.3 on 2022-04-11 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('detailed_movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='category name')),
                ('category_name_en', models.CharField(blank=True, max_length=50, null=True, verbose_name='category name')),
                ('category_name_ru', models.CharField(blank=True, max_length=50, null=True, verbose_name='category name')),
                ('category_name_uz', models.CharField(blank=True, max_length=50, null=True, verbose_name='category name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('created_at_en', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at')),
                ('created_at_ru', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at')),
                ('created_at_uz', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='MoviesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='name')),
                ('name_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='name')),
                ('name_ru', models.CharField(blank=True, max_length=100, null=True, verbose_name='name')),
                ('name_uz', models.CharField(blank=True, max_length=100, null=True, verbose_name='name')),
                ('year', models.DateTimeField(blank=True, null=True, verbose_name='year')),
                ('ratingMovie', models.CharField(max_length=10, verbose_name='rating of Movie')),
                ('duration', models.CharField(max_length=10, verbose_name='duration')),
                ('presented_description', models.TextField(blank=True, null=True, verbose_name='presented description')),
                ('presented_description_en', models.TextField(blank=True, null=True, verbose_name='presented description')),
                ('presented_description_ru', models.TextField(blank=True, null=True, verbose_name='presented description')),
                ('presented_description_uz', models.TextField(blank=True, null=True, verbose_name='presented description')),
                ('detailed_description', models.TextField(blank=True, null=True, verbose_name='detailed description')),
                ('detailed_description_en', models.TextField(blank=True, null=True, verbose_name='detailed description')),
                ('detailed_description_ru', models.TextField(blank=True, null=True, verbose_name='detailed description')),
                ('detailed_description_uz', models.TextField(blank=True, null=True, verbose_name='detailed description')),
                ('film', models.FileField(blank=True, null=True, upload_to='media/videos/', verbose_name='film')),
                ('poster_img', models.ImageField(blank=True, null=True, upload_to='media/posters/&Y/%m/%d/', verbose_name='Poster of movies')),
                ('logo_img', models.ImageField(blank=True, null=True, upload_to='media/logos/', verbose_name='Logo of Movie')),
                ('tv_show', models.BooleanField(default=False, verbose_name='tv show')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('award', models.ManyToManyField(related_name='movies', to='detailed_movies.awardsmodel', verbose_name='award')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movies', to='movies.categorymodel', verbose_name='category')),
                ('director', models.ManyToManyField(related_name='movies', to='detailed_movies.directormodel', verbose_name='director')),
                ('producer', models.ManyToManyField(related_name='movies', to='detailed_movies.producermodel', verbose_name='producer')),
                ('screenplay', models.ManyToManyField(related_name='movies', to='detailed_movies.screenplaymodel', verbose_name='screenplay')),
                ('tag', models.ManyToManyField(related_name='movies', to='movies.tagmodel', verbose_name='tags')),
            ],
            options={
                'verbose_name': 'movie',
                'verbose_name_plural': 'movies',
            },
        ),
    ]
