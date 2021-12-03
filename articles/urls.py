from django.urls import path, include
from rest_framework_nested import routers
from .views import ArticleViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register('articles', ArticleViewSet, basename='article')

comments_router = routers.NestedDefaultRouter(router, 'articles', lookup='article')
comments_router.register('comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(comments_router.urls)),
]
