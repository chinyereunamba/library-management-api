from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer
from .models import Account, Student, Admin


class AdminProfile(serializers.ModelSerializer):
    class Meta:
        fields = ['phone_number',]

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='student.user', read_only=True)
    class Meta:
        fields = ['id', 'user', 'fee']
        model = Student

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Account

class CustomUserSerializer(UserDetailsSerializer):
    admin_profile = AdminProfile()
    class Meta(UserDetailsSerializer.Meta):
        fields = [UserDetailsSerializer.fields, 'admin_profile', ]