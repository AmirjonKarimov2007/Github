# Generated by Django 5.0 on 2024-09-29 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='profile_photos/default_profile.webp', null=True, upload_to='profile_photos'),
        ),
    ]
