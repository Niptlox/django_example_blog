# Generated by Django 3.2.7 on 2021-09-15 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210915_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_introduction',
            field=models.TextField(default='', verbose_name='Вступление статьи'),
            preserve_default=False,
        ),
    ]