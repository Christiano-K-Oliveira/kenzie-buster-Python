# 1
# class LoginView(APIView):
#     def post(self, request: Request) -> Response:
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         user = authenticate(**serializer.validated_data)

#         if not user:
#             return Response({"detail": "No active account found with the given credentials"}, status.HTTP_401_UNAUTHORIZED)

#         refresh = RefreshToken.for_user(user)
#         token_dict = {
#             "refresh": str(refresh),
#             "access": str(refresh.access_token)
#         }

#         return Response(token_dict, status.HTTP_200_OK)


# 2
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# class LoginView(APIView):
#     def post(self, request: Request) -> Response:
#         serializer = TokenObtainPairSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         return Response(serializer.validated_data, status.HTTP_200_OK)

# 3
# from rest_framework_simplejwt.views import TokenObtainPairView


# class LoginView(TokenObtainPairView):
#     def post(self, request: Request) -> Response:
#         serializer = TokenObtainPairSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         return Response(serializer.validated_data, status.HTTP_200_OK)


# 4
# class IsCustom(BasePermission):
#     def has_permission(self, request: Request, view):
#         if request.method == "POST":
#             return 
