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
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]