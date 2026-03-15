from rest_framework import serializers
from note.models import Todo
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'author']
        extra_kwargs = {'author': {'read_only': True}}

        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self,validated_data):
        # print('validated_data', validated_data)
        user = User.objects.create_user(**validated_data)
        return user
     