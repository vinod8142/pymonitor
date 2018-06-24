from rest_framework import serializers
from users.models import *
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class UserSerializer(serializers.ModelSerializer):
    #reg = UserRegisterSerializer(many=True, source='reg_user')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email')

class UserRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserRegister
        fields = ('hometown','mobile_no','user')




