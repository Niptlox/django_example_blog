# Generated by Django 3.2.7 on 2021-09-17 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_article_url_image_introduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url_image_introduction',
            field=models.URLField(blank=True, default='', verbose_name='Ссылка на картинку вступления'),
        ),
    ]
