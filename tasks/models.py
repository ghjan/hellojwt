from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    title = models.CharField(max_length=100)
    person = models.ForeignKey(User)
    due_to = models.DateTimeField()

    def __str__(self):
        return 'Task with title: {}'.format(self.title)