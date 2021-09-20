from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:article_id>', views.article, name='article'),
    path('article/<int:article_id>/post_comment', views.post_comment, name='post_comment'),
    path('article/create', views.article_create, name='article_create'),
    path('article/<int:article_id>/edit', views.article_edit, name='article_edit'),
    path('article/<int:article_id>/del', views.article_del, name='article_del'),
    # path('register', views.user_register, name='register'),
    # path('login', views.user_login, name='login'),
    path("profile", views.profile, name="profile"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
]