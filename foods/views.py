from django.conf import settings
from rest_framework import viewsets, mixins
from .serializers import FoodCategoryRetreiveSerializer, FoodCategorySerializer, FoodListSerializer, FoodRetreiveSerializer, FoodSerializer, FoodReviewSerializer
from .models import FoodCategory, Food, FoodReview, RateTypes


class FoodCategoryViewSet(viewsets.ModelViewSet):

    queryset = FoodCategory.objects.all() 
    serializer_class = FoodCategorySerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return FoodCategoryRetreiveSerializer
        
        return super(FoodCategoryViewSet, self).get_serializer_class()


class FoodViewSet(viewsets.ModelViewSet):
 
    serializer_class = FoodSerializer
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return FoodRetreiveSerializer

        if self.action == 'list':
            return FoodListSerializer

        return super(FoodViewSet, self).get_serializer_class()
    
    def get_queryset(self):
        queryset = Food.objects.all()
        query = self.request.query_params.get('query')
        if query is not None:
            queryset = queryset.filter(name__icontains=query)

        return queryset


class FoodReviewViewSet(viewsets.ModelViewSet):

    queryset = FoodReview.objects.all()
    serializer_class = FoodReviewSerializer

    def perform_create(self, serializer):
        food = Food.objects.get(pk=self.kwargs['food_pk'])
        serializer.save(author=self.request.user, food=food)