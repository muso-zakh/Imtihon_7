from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Register
  
from rest_framework import serializers


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = Register
        fields = ['first_name',
                  'last_name',
                  'email',
                  'organization',
                  'login',
                  'password',
                  'password2',
                  'scientific_degree',
                  'username']
        read_only_fields =  ('id',) 

    def create(self, validated_data):
        user = Register.objects.create_user(
            username = validated_data.get('username'),
            first_name = validated_data.get('first_name'),
            last_name = validated_data.get('last_name'),
            email = validated_data.get('email'),
            organization = validated_data.get('organization'),
            login = validated_data.get('login'),
            password = validated_data.get('password'),
            scientific_degree = validated_data.get('scientific_degree')
        )
        return user


class Profile(ModelSerializer):
    class Meta:
        model = Register
        fields = ['first_name',
                  'last_name',
                  'email',
                  'organization',
                  'login',
                  'scientific_degree',
                  'username']
        read_only_fields =  ('id',) 


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(label=('Username'))
    password = serializers.CharField(write_only=True, label=('Password'))
