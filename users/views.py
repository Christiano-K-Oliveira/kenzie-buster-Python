from rest_framework.views import APIView, status, Request, Response
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from .serializers import RegistroSerializer, LoginSerializer
from users.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsUserId, IsCustom


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
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)

        if not user:
            return Response({"detail": "No active account found with the given credentials"}, status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        token_dict = {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }

        return Response(token_dict, status.HTTP_200_OK)


class UsersIdView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserId]

    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, user)

        serializer = RegistroSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, user)

        serializer = RegistroSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
