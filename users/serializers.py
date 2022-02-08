from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password',
                'first_name', 'last_name', 'bio', 'profile_picture',
                'followers', 'following', 'last_login', 'date_joined']

