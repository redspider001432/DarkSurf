# Generated by Django 4.1.2 on 2022-10-15 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_likepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='post_images'),
        ),
    ]