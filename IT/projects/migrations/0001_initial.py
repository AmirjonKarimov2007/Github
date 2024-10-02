# Generated by Django 5.0 on 2024-09-27 12:26

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('demo_link', models.CharField(blank=True, max_length=400, null=True)),
                ('source_link', models.CharField(blank=True, max_length=400, null=True)),
                ('vote_count', models.IntegerField(default=0)),
                ('vote_radio', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('body', models.TextField(default='')),
                ('value', models.CharField(choices=[('+', 'Ijobiy'), ('-', 'Salbiy')], max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_review', to='projects.project')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='project_tag', to='projects.tag'),
        ),
    ]
