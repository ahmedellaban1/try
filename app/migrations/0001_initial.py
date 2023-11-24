# Generated by Django 4.2.4 on 2023-11-24 08:48

from django.db import migrations, models
import etc.file_uploader
import etc.uploader


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=etc.uploader.Uploader.model_image_uploader)),
            ],
        ),
        migrations.CreateModel(
            name='Model2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=etc.file_uploader.model2_image_uploader)),
            ],
        ),
    ]
