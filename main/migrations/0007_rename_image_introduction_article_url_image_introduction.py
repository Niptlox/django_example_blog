# Generated by Django 3.2.7 on 2021-09-15 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_article_image_introduction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='image_introduction',
            new_name='url_image_introduction',
        ),
    ]
