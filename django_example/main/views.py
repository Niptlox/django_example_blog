from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Article


# Create your views here.


def index(request):
    last_articles = Article.objects.order_by('-pub_date')[:5]
    print(last_articles)
    return render(request, 'main/list.html', {"last_articles": last_articles})


def article(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Статья не найдена!")
    c = a.comment_set.order_by('-id')[:10]
    return render(request, 'main/article.html', {"article": a, "last_comments": c})


def post_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Статья не найдена!")

    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse("main:article", args=(a.id, )))
