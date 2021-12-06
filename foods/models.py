from django.contrib.auth import get_user_model
from django.db import models
from enumchoicefield import ChoiceEnum, EnumChoiceField
from deufood.utils import random_filename


class RateTypes(ChoiceEnum):
    호 = "호"
    보통 = "보통"
    불호 = "불호"
 

class FoodCategory(models.Model):

    name = models.CharField(max_length=40, primary_key=True)
    description = models.CharField(max_length=200, null=False, blank=False)
    thumbnail = models.ImageField(upload_to=random_filename, null=False, blank=False)

    def __str__(self):
        return f'{self.pk}' 


class Food(models.Model):

    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(FoodCategory, related_name='foods', on_delete=models.PROTECT)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=2000, null=False)
    price = models.IntegerField()
    thumbnail = models.ImageField(upload_to=random_filename, null=False, blank=False)

    def __str__(self):
        return f'[{self.id}] {self.category} :: {self.name}'


class FoodReview(models.Model):

    id = models.AutoField(primary_key=True)
    food = models.ForeignKey(Food, related_name='reviews', on_delete=models.PROTECT)
    author = models.ForeignKey(get_user_model(), related_name='food_reviews', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    rate = EnumChoiceField(RateTypes)
    contents = models.TextField(null=False)

    def __str__(self):
        return f'[{self.id}] {self.food} :: {self.author}'
