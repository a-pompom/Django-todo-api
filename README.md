# Django API Todo List

DjangoでAPIを利用したTODOリストを作成。

## プロジェクト・アプリ作成

以下コマンドを実行。

* django-admin startproject config .
* python3 manage.py startapp api_todo

## ディレクトリ構成

### プロジェクト

* settings.py プロジェクト固有の設定を記述 DBの接続情報や利用するアプリなど
* urls.py URLパターンとビューのマッチング情報を記述
* wsgi.py WSGIインタフェースを利用してDjangoプロジェクトを起動するためのエントリポイント

### アプリ

* admin.py 管理サイトに関する記述をするためのモジュール
* apps.py アプリを識別するための設定
* migrations DBとPythonオブジェクトをマッピングするためのモジュール
* models.py モデルの定義を行う
* tests.py テストコードを記述
* views.py ビューを記述


## 基本設定

### プロジェクトへアプリを登録

settings.pyのINSTALLED_APPSへ以下を追記

* 'api_todo.apps.ApiTodoConfig'

### データベースの接続情報を設定

settings.pyのDATABASESを書き換える

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_api_todo',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '',
    }
}

### URL情報を追記

プロジェクトのurls.pyへ以下を追記

* path('api_todo/', include('api_todo.urls')),

※ includeをimportしておく

アプリ側にもurls.pyを作成し、以下を追記

```python
from django.urls import path
from .views import APITodoView

urlpatterns = [
        path('', APITodoView.as_view(), name='home'),
]
```


### クラスベースViewを作成

views.pyを以下のように作成

```python
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
```

## 動作確認

以下コマンドを実行。

* python3 manage.py runserver
* curl http://localhost:8000/api_todo -L

上記により、レスポンスとしてJSONが得られる。

## DBのテーブル作成

modelを作成後、以下コマンドを実行。

* python3 manage.py makemigrations api_todo
* python3 manage.py migrate api_todo

コマンドを実行後、DB上にテーブルが作成される

## RESTフレームワークの導入

settings.pyのINSTALLED_APPSへ、「rest_framework」を追記することで利用可能となる。 