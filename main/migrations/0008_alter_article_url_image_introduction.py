# Generated by Django 3.2.7 on 2021-09-17 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_image_introduction_article_url_image_introduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url_image_introduction',
            field=models.URLField(default='', null=True, verbose_name='Ссылка на картинку вступления'),
        ),
    ]
