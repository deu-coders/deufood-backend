from django.conf import settings
from django.db.models import Count, F
from rest_framework import viewsets, mixins
from rest_framework.response import Response
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


class Best5FoodViewSet(viewsets.ViewSet):

    def list(self, request):
        results = FoodReview.objects \
            .filter(rate=RateTypes.호) \
            .select_related('food') \
            .values('food') \
            .annotate(likes=Count('rate')) \
            .values(
                id=F('food__id'),
                category=F('food__category'),
                name=F('food__name'),
                description=F('food__description'),
                price=F('food__price'),
                thumbnail=F('food__thumbnail'),
                likes=F('likes'),
            ) \
            .order_by('-likes')[:5]

        for result in results:
            result['thumbnail'] = request.build_absolute_uri(settings.MEDIA_URL + result['thumbnail'])

        return Response(results)
