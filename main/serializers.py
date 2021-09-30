from rest_framework import serializers

from main.models import Article

from django.contrib.auth.models import User


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'article_title', 'article_introduction', 'introduction_img', 'pub_date', 'username')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'username')
