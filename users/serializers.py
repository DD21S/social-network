from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'last_login', 'username', 'first_name', 'last_name',
                    'date_joined', 'bio', 'profile_picture']
        read_only_fields = ['id', 'last_login', 'username', 'date_joined']


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name',
                    'bio', 'profile_picture']


class DeleteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password']   

