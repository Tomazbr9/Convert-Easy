# Generated by Django 5.1.2 on 2024-10-25 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convertlt', '0002_alter_fileupload_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='file',
            field=models.FileField(upload_to='conversions/'),
        ),
    ]