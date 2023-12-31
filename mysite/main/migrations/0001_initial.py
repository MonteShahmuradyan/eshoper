# Generated by Django 4.2.1 on 2023-06-02 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeCarusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=100, verbose_name='Carusel name1')),
                ('name2', models.CharField(max_length=100, verbose_name='Carusel name2')),
                ('about', models.TextField(verbose_name='Carusel about')),
                ('button_name', models.CharField(max_length=40, verbose_name='Carusel button name')),
                ('img', models.ImageField(upload_to='index_images', verbose_name='Carusel image')),
                ('price_image', models.ImageField(upload_to='index_images', verbose_name='Carusel price image')),
            ],
        ),
        migrations.CreateModel(
            name='HomeCaruselActive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=100, verbose_name='Carusel name1')),
                ('name2', models.CharField(max_length=100, verbose_name='Carusel name2')),
                ('about', models.TextField(verbose_name='Carusel about')),
                ('button_name', models.CharField(max_length=40, verbose_name='Carusel button name')),
                ('img', models.ImageField(upload_to='index_images', verbose_name='Carusel image')),
                ('price_image', models.ImageField(upload_to='index_images', verbose_name='Carusel price image')),
            ],
        ),
    ]
