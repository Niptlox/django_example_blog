# views.py
from rest_framework import viewsets

from django.http import HttpRequest
from rest_framework.response import Response

from main.serializers import ArticleSerializer, UserSerializer
from main.models import Article, User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-pub_date')
    serializer_class = ArticleSerializer

    @staticmethod
    def get_context_data(self, i=0):  # request: HttpRequest,
        queryset = Article.objects.all().order_by('-pub_date')[i:i + 5]
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        start_i = int(self.request.query_params.get('i') or 0)
        queryset = Article.objects.all().order_by('-pub_date')[start_i:start_i + 5]

        return queryset
