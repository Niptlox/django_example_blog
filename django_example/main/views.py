from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpRequest
from django.urls import reverse
from django.utils import timezone

from .models import Article

# Create your views here.


def index(request: HttpRequest):
    last_articles = Article.objects.order_by('-pub_date')[:5]
    print(last_articles)
    return render(request, 'main/list.html', {"last_articles": last_articles})


def article(request: HttpRequest, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Статья не найдена!")
    c = a.comment_set.order_by('-id')[:10]
    return render(request, 'main/article.html', {"article": a, "last_comments": c})


def article_edit(request: HttpRequest):
    if request.method == "POST":
        a = Article(article_title=request.POST['name'], article_text=request.POST['text'], pub_date=timezone.now())
        a.save()
        return HttpResponseRedirect(reverse("main:index"))
    else:
        return render(request, 'main/article_edit.html')


def post_comment(request: HttpRequest, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Статья не найдена!")

    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse("main:article", args=(a.id, )))
