from django.test import TestCase
from django.urls import reverse
import json

from .models import TodoItem

class GetRequestTests(TestCase):

    def setUp(self):
        self.task = TodoItem.objects.create(
            task_name = 'task1',
            done = False
        )

    def test_Getリクエストでタスクの一覧が取得できる(self):
        print(json.loads(json.loads(self.client.get(reverse('home')).content)["todoList"])[0]["fields"])
        print('hello')
        self.assertEqual('', '')