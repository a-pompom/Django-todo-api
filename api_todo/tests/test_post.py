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

    def test_POSTリクエストでタスクが登録される(self):
        TARGET_URL = '/api_todo/'

        params = {
            'task_name': 'post_task',
            'done': True
        }

        response = self.client.post(TARGET_URL, params, format='json')

        self.assertEqual(TodoItem.objects.count(), 2)
        self.assertEqual(response.status_code, 201)

        item = TodoItem.objects.filter(task_name='post_task')[0]
        expected = {
            'id': item.id,
            'task_name': item.task_name,
            'done': item.done
        }

        actual = response.content

        self.assertJSONEqual(actual, expected)

    def test_POSTリクエストでエラー発生時に登録が失敗する(self):

        TARGET_URL = '/api_todo/'

        params = {
            'task_name': '',
            'done': True
        }

        response = self.client.post(TARGET_URL, params, format='json')

        self.assertEqual(TodoItem.objects.count(), 1)
        self.assertEqual(response.status_code, 400)
        
        # エラーメッセージを検証
        actual = json.loads(response.content)['task_name'][0]
        expected = 'タスク名を入力してください。'

        self.assertEqual(actual, expected)