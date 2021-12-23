# Generated by Django 4.0 on 2021-12-19 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=2500)),
                ('review_rating', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('imdb_id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=55)),
                ('runtime', models.CharField(max_length=55)),
                ('genre', models.CharField(max_length=255)),
                ('director', models.CharField(max_length=255)),
                ('writer', models.CharField(max_length=255)),
                ('actor', models.CharField(max_length=255)),
                ('plot', models.TextField(max_length=2500)),
                ('language', models.CharField(max_length=255)),
                ('poster', models.URLField()),
                ('type', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=10000)),
                ('movie_rating', models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movies.movie')),
            ],
        ),
    ]