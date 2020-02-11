from django.views.generic import View
from django.http import JsonResponse

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

        return JsonResponse({'message': 'Hello World'})