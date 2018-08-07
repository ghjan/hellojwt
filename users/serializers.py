# _*_ coding: utf-8 _*_

from rest_framework import serializers
# from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()


#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User

class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()
    tasks = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True
    )

    # 重写create方法
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta(object):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',
                  'date_joined', 'password',
                  'tasks'
                  )

        extra_kwargs = {'password': {'write_only': True}}
