# Generated by Django 5.1.2 on 2024-10-24 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='upload/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]