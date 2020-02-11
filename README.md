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
