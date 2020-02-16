from rest_framework import serializers
from .models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'
        extra_kwargs = {
            'task_name': {
                'error_messages': {
                    'blank': 'タスク名を入力してください。',
                }
            },
            'done': {
                'error_messages': {
                    'invalid': '完了判定が正しくありません。'
                }
            }
        }

class TodoItemListSerializer(serializers.ListSerializer):
    child = TodoItemSerializer