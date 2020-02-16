from rest_framework import status, views
from rest_framework.response import Response
from django.db.models import F
from django.shortcuts import get_object_or_404

from .models import TodoItem
from .serializers import TodoItemSerializer, TodoItemListSerializer

class APITodoView(views.APIView):
    """
    Todoリストで扱うAPIを管理するためのViewクラス
    """
    
    def get(self, request, *args, **kwargs):
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
        response : Response
        APIのレスポンスとして渡されるJSONデータ
        """

        todoItemList = TodoItem.objects.all()

        # many=Trueを設定することで、ListSerializerを利用
        serializer = TodoItemSerializer(instance=todoItemList, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        
        serializer = TodoItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class APITodoUpdateView(views.APIView):
    def put(self, request, pk, *args, **kwargs):
        todoItem = get_object_or_404(TodoItem, pk=pk)

        serializer = TodoItemSerializer(instance=todoItem, data=request.data)
        serializer.is_valid()

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        todoItem = get_object_or_404(TodoItem, pk=pk)

        todoItem.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
