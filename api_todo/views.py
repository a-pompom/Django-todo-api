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
        APIのレスポンスとして渡されるJSONデータ タスクの一覧を保持
        """

        todoItemList = TodoItem.objects.all()

        # many=Trueを設定することで、ListSerializerを利用
        serializer = TodoItemSerializer(instance=todoItemList, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        postリクエストで呼び出される処理
        Parameters
        ----------
        self : Object
            APITodoView
        request : HttpRequest
            apiへのHttpRequest
        Returns
        -------
        response : Response
        APIのレスポンスとして渡されるJSONデータ 登録されたタスクを保持
        """
        
        # シリアライザでJSONをPythonオブジェクトへ変換し、
        # 変換時にバリデーションを行う
        serializer = TodoItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # シリアライズされたオブジェクトでDBへ登録
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class APITodoUpdateView(views.APIView):
    """
    Todoリストの更新処理で扱うAPIを管理するためのViewクラス
    """

    def put(self, request, pk, *args, **kwargs):
        """
        putリクエストで呼び出される処理
        Parameters
        ----------
        self : Object
            APITodoUpdateView
        request : HttpRequest
            apiへのHttpRequest
        pk  : int
            更新対象を識別するためのプライマリーキー(本来はUUIDで特定されないような要素にするのが望ましい)
        Returns
        -------
        response : Response
        APIのレスポンスとして渡されるJSONデータ 更新されたタスクを保持
        """

        # 引数で渡された主キーからタスクをDBより取得
        todoItem = get_object_or_404(TodoItem, pk=pk)

        # パラメータをもとにシリアライザを構築し、過程でバリデーション
        serializer = TodoItemSerializer(instance=todoItem, data=request.data)
        serializer.is_valid()

        # 更新処理
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        """
        deleteリクエストで呼び出される処理
        Parameters
        ----------
        self : Object
            APITodoUpdateView
        request : HttpRequest
            apiへのHttpRequest
        pk  : int
            削除対象を識別するためのプライマリーキー(本来はUUIDで特定されないような要素にするのが望ましい)
        Returns
        -------
        response : Response
        削除結果を格納したレスポンス
        """

        todoItem = get_object_or_404(TodoItem, pk=pk)

        todoItem.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)