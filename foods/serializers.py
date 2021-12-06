from rest_framework import serializers
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from users.permissions import IsAuthorOrReadOnly
from .models import Food, FoodCategory, FoodReview


class FoodReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodReview
        fields = '__all__'
        read_only_fields = ['author', 'food']

    permission_classes = [IsAuthorOrReadOnly]
    author = serializers.CharField(source='author.username', read_only=True)


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = '__all__'

    permission_classes = [IsAuthenticatedOrReadOnly]
    thumbnail = serializers.ImageField(required=False, allow_empty_file=True)


class FoodListSerializer(FoodSerializer):
    reviews = serializers.SerializerMethodField()

    def get_reviews(self, obj):
        return obj.reviews.count()


class FoodRetreiveSerializer(FoodSerializer):

    reviews = FoodReviewSerializer(many=True, read_only=True)


class FoodCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodCategory
        fields = '__all__'

    permission_classes = [IsAdminUser]


class FoodCategoryRetreiveSerializer(FoodCategorySerializer):

    foods = FoodListSerializer(many=True, read_only=True)