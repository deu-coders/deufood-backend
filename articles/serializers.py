from rest_framework import serializers
from articles.models import Article, Comment
from users.permissions import IsAuthorOrReadOnly


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['article']

    permission_classes = [IsAuthorOrReadOnly]
    author = serializers.CharField(source='author.username', read_only=True)


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['author']

    permission_classes = [IsAuthorOrReadOnly]
    thumbnail = serializers.ImageField(required=False, allow_empty_file=True)
    comments = serializers.SerializerMethodField()
    author = serializers.CharField(source='author.username', read_only=True)

    def get_comments(self, obj):
        return obj.comments.count()


class ArticleRetrieveSerializer(ArticleSerializer):

    comments = CommentSerializer(many=True, read_only=True)