from django.db.models import query
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer
from rest_framework import generics, serializers
from rest_framework.permissions import AllowAny


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = RegistrationSerializer
