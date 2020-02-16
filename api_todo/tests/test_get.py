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

    def test_GETリクエストでステータスコード200が得られる(self):

        TARGET_URL = '/api_todo/'

        response = self.client.get(TARGET_URL, None, format='json')

        self.assertEqual(response.status_code, 200)

    def test_GETリクエストでTODOリストのJSONオブジェクトが得られる(self):

        TARGET_URL = '/api_todo/'

        response = self.client.get(TARGET_URL, None, format='json')

        responseJSON = json.loads(response.content)[0]
        actual = {'task_name': responseJSON['task_name'], 'done': responseJSON['done']}
        expected = {'task_name': 'task1', 'done': False}

        print(actual)
        print(expected)

        self.assertEqual('', '')