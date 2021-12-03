from rest_framework import viewsets
from users.permissions import IsAuthorOrReadOnly
from .serializers import ArticleRetrieveSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment


class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ArticleRetrieveSerializer
        
        return super(ArticleViewSet, self).get_serializer_class()


class CommentViewSet(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(article=self.kwargs['article_pk'])

    def perform_create(self, serializer):
        article = Article.objects.get(pk=self.kwargs['article_pk'])
        serializer.save(author=self.request.user, article=article)
