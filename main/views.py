from django.http import HttpResponseRedirect, Http404, HttpRequest, HttpResponseForbidden
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import NewUserForm
from .models import Article


# Create your views here.

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="main/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main:index")


def profile(request: HttpRequest):
    return render(request, 'main/profile.html')


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


def article_create(request: HttpRequest):
    current_user = request.user
    if not request.user.is_authenticated:
        Http404("Пользователь не авторизован!")
    if request.method == "POST":
        a = Article(user=current_user,
                    article_title=request.POST['name'],
                    article_text=request.POST['text'].replace("<script", "<scripts"),
                    article_introduction=request.POST['intro'].replace("<script", "<scripts"),
                    pub_date=timezone.now(),
                    )
        a.save()
        return HttpResponseRedirect(reverse("main:index"))
    else:
        return render(request, 'main/article_edit.html', {"article": None})


def article_del(request: HttpRequest, article_id):
    if not request.user.is_authenticated:
        Http404("Пользователь не авторизован!")
    try:
        a: Article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Статья не найдена!")
    if not a.user or a.user.id != request.user.id:
        return HttpResponseForbidden("Ошибка доступа! " + str(a.user))
    a.delete()
    return HttpResponseRedirect(reverse("main:profile"))


def article_edit(request: HttpRequest, article_id):
    if not request.user.is_authenticated:
        Http404("Пользователь не авторизован!")
    try:
        a: Article = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Статья не найдена!")
    if not a.user or a.user.id != request.user.id:
        return HttpResponseForbidden("Ошибка доступа! " + str(a.user))

    if request.method == "POST":
        a.article_title = request.POST['name']
        a.article_text = request.POST['text'].replace("<script", "<scripts")
        a.article_introduction = request.POST['intro'].replace("<script", "<scripts")
        a.pub_date = timezone.now()
        a.save()
        return HttpResponseRedirect(reverse("main:profile"))
    else:
        return render(request, 'main/article_edit.html', {"article": a})


def post_comment(request: HttpRequest, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404("Статья не найдена!")

    a.comment_set.create(author_name=request.user.username, comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse("main:article", args=(a.id,)) + "#comments")


def user_register(request: HttpRequest):
    if request.method == "POST":
        username, login, password = request.POST['username'], request.POST['login'], request.POST['password']
        return HttpResponseRedirect(reverse("main:login"))
    else:
        return render(request, 'main/user_register.html')


def user_login(request: HttpRequest):
    if request.method == "POST":
        login, password = request.POST['login'], request.POST['password']
        return HttpResponseRedirect(reverse("main:index"))
    else:
        return render(request, 'main/user_login.html')
