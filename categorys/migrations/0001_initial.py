# Generated by Django 3.2.16 on 2022-12-13 05:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('deleted_at', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
