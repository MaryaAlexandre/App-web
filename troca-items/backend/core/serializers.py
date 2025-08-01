from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Item

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user

class ItemSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True) # Exibe os detalhes do dono, mas não permite a escrita

    class Meta:
        model = Item
        fields = ['id', 'name', 'description', 'image', 'condition', 'owner', 'created_at']
        read_only_fields = ['owner']