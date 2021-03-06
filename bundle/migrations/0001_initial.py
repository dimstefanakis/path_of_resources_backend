# Generated by Django 3.2.7 on 2021-09-30 21:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_id', models.CharField(blank=True, max_length=30, null=True)),
                ('name', models.CharField(max_length=100)),
                ('airtable_url', models.URLField(blank=True, null=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='bundle_images')),
            ],
        ),
    ]
