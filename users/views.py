from rest_framework.views import APIView, status, Request, Response
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from .serializers import RegistroSerializer
from users.models import User
import ipdb


# Create your views here.
class UsersView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = RegistroSerializer(users, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = RegistroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class LoginView(APIView):
    ...
