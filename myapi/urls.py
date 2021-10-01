from django.urls import path
from . import views

app_name = "myapi"
# urlpatterns = [
#     path('articles/', views.GetCapitalInfoView.as_view()),
# ]

# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'article', views.ArticleViewSet)
router.register(r'user', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('/', include(router.urls), name="article"),
    path('/', include(router.urls)),
    path('/manyArticles/<int:count>/<str:title>', views.create_many_articles, name='create_many_articles'),
    path('/delManyArticles/<int:idStart>/<int:idEnd>', views.del_many_articles, name='create_many_articles'),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]