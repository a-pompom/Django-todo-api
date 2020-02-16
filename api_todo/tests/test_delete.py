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

    def test_DELETEリクエストでタスクが削除される(self):
        pk = TodoItem.objects.filter(task_name='task1')[0].id

        url = reverse('home_pk', kwargs={'pk': pk})


        print(url)
        response = self.client.delete(url)

        self.assertEqual(TodoItem.objects.count(), 0)

        self.assertEqual(response.status_code, 204)