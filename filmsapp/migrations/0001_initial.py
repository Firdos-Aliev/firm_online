# Generated by Django 3.1.5 on 2021-01-25 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('about', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('about', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанр',
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Имя')),
                ('surname', models.CharField(max_length=128, verbose_name='Фамилия')),
                ('age', models.PositiveSmallIntegerField(blank=True, verbose_name='Возраст')),
                ('about', models.TextField(blank=True, verbose_name='Описание')),
                ('img', models.ImageField(blank=True, upload_to='participants/', verbose_name='Фотография')),
                ('role', models.CharField(max_length=128, verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Участники',
                'verbose_name_plural': 'Участники',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('about', models.TextField(blank=True, verbose_name='Описание')),
                ('img', models.ImageField(blank=True, upload_to='movies/', verbose_name='Постер')),
                ('year', models.PositiveSmallIntegerField(blank=True, verbose_name='Год')),
                ('budget', models.PositiveBigIntegerField(blank=True, verbose_name='Бюджет')),
                ('country', models.CharField(blank=True, max_length=128, verbose_name='Срана')),
                ('video', models.FileField(blank=True, upload_to='videos/', verbose_name='Видео')),
                ('is_active', models.BooleanField(default=False, verbose_name='Активный')),
                ('actors', models.ManyToManyField(blank=True, related_name='film_actors', to='filmsapp.Participant', verbose_name='Актеры')),
                ('category', models.ManyToManyField(blank=True, related_name='film_category', to='filmsapp.Category', verbose_name='Категория')),
                ('directors', models.ManyToManyField(blank=True, related_name='film_directors', to='filmsapp.Participant', verbose_name='Продюсер')),
                ('genres', models.ManyToManyField(blank=True, related_name='film_genres', to='filmsapp.Genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
    ]