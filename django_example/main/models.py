from django.db import models
from django.utils import timezone
import datetime


class Article(models.Model):
    article_title = models.CharField("название статьи", max_length=200)
    article_text = models.TextField("текст статьи")
    pub_date = models.DateTimeField("дата публикации")

    def __str__(self):
        return self.article_title

    def was_publish_recently(self):
        return (timezone.now() - self.pub_date) <= datetime.timedelta(days=7)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField("имя автора", max_length=50)
    comment_text = models.CharField("текст коментария", max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

