from django.views.generic import View
from django.http import JsonResponse
from django.db.models import F

from django.core import serializers

from .models import TodoItem

class APITodoView(View):
    """
    Todoリストで扱うAPIを管理するためのViewクラス
    """
    
    def get(self, request):
        """
        getリクエストで呼び出される処理
        Parameters
        ----------
        self : Object
            APITodoView
        request : HttpRequest
            apiへのHttpRequest
        Returns
        -------
        jsonResponse : JsonResponse
        APIのレスポンスとして渡されるJSONデータ
        """

        todoList = serializers.serialize('json', TodoItem.objects.all())

        return JsonResponse({'todoList': todoList})