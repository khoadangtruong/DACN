# Generated by Django 2.2 on 2020-10-22 06:36

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('keywords', models.CharField(max_length=512)),
                ('description', models.CharField(max_length=1000)),
                ('company', models.CharField(max_length=512)),
                ('address', models.CharField(blank=True, max_length=512)),
                ('phone', models.CharField(max_length=12)),
                ('fax', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(max_length=512)),
                ('smtpserver', models.CharField(blank=True, max_length=512)),
                ('smtpemail', models.CharField(blank=True, max_length=512)),
                ('smtppassword', models.CharField(blank=True, max_length=512)),
                ('smtpport', models.CharField(blank=True, max_length=20)),
                ('icon', models.ImageField(blank=True, upload_to='images/')),
                ('facebook', models.CharField(blank=True, max_length=50)),
                ('instagram', models.CharField(blank=True, max_length=50)),
                ('twitter', models.CharField(blank=True, max_length=50)),
                ('youtube', models.CharField(blank=True, max_length=50)),
                ('aboutus', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('contact', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('references', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
