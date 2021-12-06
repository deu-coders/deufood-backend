from django.urls import path,include 
from rest_framework_nested import routers 
from .views import Best5FoodViewSet, FoodViewSet, FoodReviewViewSet, FoodCategoryViewSet

router = routers.DefaultRouter()
router.register('foods', FoodViewSet, basename='food')
router.register('food_categories', FoodCategoryViewSet, basename='food_categories')
router.register('best_foods', Best5FoodViewSet, basename='best_foods')

reviews_router = routers.NestedDefaultRouter(router, 'foods', lookup='food')
reviews_router.register('reviews', FoodReviewViewSet, basename='review')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(reviews_router.urls)),
]
