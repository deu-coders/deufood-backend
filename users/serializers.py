from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username']

    def create(self, request):
        user = User.objects.create_user(
            username=request['username'],
            password=request['password'],
        )
        return user
