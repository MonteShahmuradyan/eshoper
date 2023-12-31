# Generated by Django 4.2.1 on 2023-06-05 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_product_options_alter_product_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Product name')),
                ('price', models.PositiveIntegerField(verbose_name='Product price')),
                ('img', models.ImageField(upload_to='index_images', verbose_name='Product image')),
                ('logo', models.ImageField(blank=True, upload_to='index_images', verbose_name='Product image logo')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Product create date')),
                ('sub_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_key', to='main.panel')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
