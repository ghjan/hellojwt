from django.db import models

from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Task(models.Model):
    title = models.CharField(max_length=100)
    person = models.ForeignKey(User, related_name='tasks', blank=True)
    due_to = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Task with title: {}'.format(self.title)
