# Generated by Django 4.2.4 on 2023-11-24 08:48

from django.db import migrations, models
import etc.uploader


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model1',
            name='img',
            field=models.ImageField(upload_to=etc.uploader.Uploader.model_image_uploader),
        ),
    ]
