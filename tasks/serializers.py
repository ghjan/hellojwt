# _*_ coding: utf-8 _*_
from rest_framework import serializers
from .models import Task
from django.contrib.auth import get_user_model

User = get_user_model()


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task



