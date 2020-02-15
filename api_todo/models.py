from django.db import models

class TodoItem(models.Model):

    class Meta:
        db_table = 'task'

    # タスク名
    task_name = models.CharField(max_length=255)

    # タスクが完了したか
    done = models.BooleanField(default=False)