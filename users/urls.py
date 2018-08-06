# _*_ coding: utf-8 _*_

from django.conf.urls import url
from .views import CreateUserAPIView

urlpatterns = [
    url(r'^create/$', CreateUserAPIView.as_view()),
]
