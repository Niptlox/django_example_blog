# Generated by Django 3.2.7 on 2021-09-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_article_article_introduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_introduction',
            field=models.URLField(default='', verbose_name='Ссылка на картинку вступления'),
        ),
    ]