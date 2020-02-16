from rest_framework.test import APITestCase
from django.urls import reverse
import json

from api_todo.models import TodoItem

class GetRequestTests(APITestCase):

    def setUp(self):
        self.task = TodoItem.objects.create(
            task_name = 'task1',
            done = False
        )

    def test_PUTリクエストで既存タスクが更新される(self):
        pk = TodoItem.objects.filter(task_name='task1')[0].id
        url = reverse('home_pk', kwargs={'pk': pk})

        params = {
            'task_name': 'mod_task1',
            'done': True
        }
        response = self.client.put(url, data=params)

        item = TodoItem.objects.filter(task_name='mod_task1')[0]
        expected = {
            'id': item.id,
            'task_name': item.task_name,
            'done': item.done
        }

        actual = response.content

        self.assertJSONEqual(actual, expected)
        self.assertEqual(response.status_code, 200)