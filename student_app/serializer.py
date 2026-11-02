from rest_framework import serializers
from student_app.models import student
from django.contrib.auth.models import User

class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'


class Userserializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user