from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
import ipdb


class RegistroSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all(), message="email already registered.")], max_length=127)
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all(), message="username already taken.")])
    birthdate = serializers.DateField(allow_null=True, default=None)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    is_employee = serializers.BooleanField(allow_null=True, default=False)
    is_superuser = serializers.BooleanField(allow_null=True, default=False)

    def create(self, validated_data: dict):
        if validated_data["is_employee"]:
            if validated_data["is_employee"] is True:
                validated_data["is_superuser"] = True
        else:
            validated_data["is_superuser"] = False

        return User.objects.create_user(**validated_data)