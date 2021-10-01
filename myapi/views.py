# views.py
from rest_framework import viewsets

from django.http import HttpResponseForbidden
from django.http import HttpRequest, JsonResponse
from django.utils import timezone
from rest_framework.response import Response

from main.serializers import ArticleSerializer, UserSerializer
from main.models import Article, User, Profile


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


def create_many_articles(request: HttpRequest, count, title):
    current_user = request.user
    if current_user and current_user.profile.status == Profile.Status.ADMIN:
        ar = []
        for i in range(1, count + 1):
            a = Article(user=None,
                        article_title=f"Title: {title} #{i}",
                        article_text=f"Text: {title} #{i}",
                        article_introduction=f"Intro: {title} #{i}",
                        pub_date=timezone.now(),
                        )
            a.save()
            ar.append(a.id)
        print("ID's", ar)
        return JsonResponse({"ids": ar})
    else:
        return HttpResponseForbidden("Ошибка доступа!")


def del_many_articles(request: HttpRequest, idStart, idEnd):
    current_user = request.user
    if current_user and current_user.profile.status == Profile.Status.ADMIN:
        ar = []
        for i in range(idStart, idEnd):
            try:
                a = Article.objects.get(id=i)

                ar.append(a.id)
                a.delete()
            except Article.DoesNotExist:
                pass

        print("ID's", ar)
        return JsonResponse({"ids": ar})
    else:
        return HttpResponseForbidden("Ошибка доступа!")
