from django.urls import path
from .views import APITodoView, APITodoUpdateView

urlpatterns = [
        path('', APITodoView.as_view(), name='home'),
        path('<int:pk>/', APITodoUpdateView.as_view(), name='home_pk'),
]