from django.urls import path
from .views import APITodoView

urlpatterns = [
        path('', APITodoView.as_view(), name='home'),
]