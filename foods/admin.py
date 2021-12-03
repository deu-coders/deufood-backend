from django.contrib import admin
from .models import FoodCategory, Food, FoodReview


admin.site.register(FoodCategory)
admin.site.register(Food)
admin.site.register(FoodReview)
