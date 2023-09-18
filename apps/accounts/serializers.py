from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer
from .models import Account, Student, Admin


class AdminProfile(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    is_admin = serializers.BooleanField(source='user.is_admin')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        fields = ['id', 'first_name', 'last_name', 'user',
                  'is_admin', 'paid_fees', 'school_fees']
        model = Student


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Account


class CustomUserSerializer(UserDetailsSerializer):
    admin_profile = AdminProfile()

    class Meta(UserDetailsSerializer.Meta):
        fields = [UserDetailsSerializer.fields, 'admin_profile', ]
