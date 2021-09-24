from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class Profile(models.Model):
    user: User = models.OneToOneField(User, on_delete=models.CASCADE)
    user_img = models.CharField(max_length=200, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


class Article(models.Model):
    user: User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # article_author = models.CharField("Автор статьи", max_length=200, default="Admin")
    article_title = models.CharField("название статьи", max_length=200)
    article_text = models.TextField("текст статьи")
    article_introduction = models.TextField("Вступление статьи", default="...", max_length=500)
    introduction_img = models.CharField("картинка вступления", max_length=200, default="", blank=True)
    pub_date = models.DateTimeField("дата публикации")

    def __str__(self):
        return self.article_title

    def was_publish_recently(self):
        return (timezone.now() - self.pub_date) <= datetime.timedelta(days=7)

    def get_introduction(self):
        return self.article_text[:150]

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField("имя автора", max_length=50)
    comment_text = models.CharField("текст коментария", max_length=200)
    pub_date = models.DateTimeField("дата публикации", default=datetime.datetime(2020, 2, 20), null=True)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
