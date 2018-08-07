from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import exceptions, permissions, status, viewsets
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from .models import Task
from .serializers import TaskSerializer
from users.serializers import UserSerializer

User = get_user_model()


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
