# Generated by Django 5.0 on 2024-09-15 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Category name'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=100, verbose_name='Comment author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default='Admin', max_length=100, verbose_name='Post author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(verbose_name='Post body'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blog.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Published time'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='value',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Post rating'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Tag name'),
        ),
    ]
