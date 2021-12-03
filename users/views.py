from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from .serializers import UserSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
