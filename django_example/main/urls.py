from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:article_id>', views.article, name='article'),
    path('article/<int:article_id>/post_comment', views.post_comment, name='post_comment'),
    path('article/edit', views.article_edit, name='article_edit'),
]