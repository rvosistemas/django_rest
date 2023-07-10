from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from rest_framework import viewsets, permissions, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer, UserRegistrationSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

        # Si las credenciales son válidas, generar el token de acceso
        # Aquí puedes utilizar la biblioteca que prefieras para generar el token (por ejemplo, JWT)
        # En este ejemplo, se asume que ya tienes una función `generate_token` que recibe el usuario y devuelve el token
        # token = generate_token(user)

        # Devolver el token en la respuesta
        # return Response({"token": token}, status=status.HTTP_200_OK)
        return Response({"user": user}, status=status.HTTP_200_OK)


# class UserLogoutView(LogoutView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         # Invalidar el token de autenticación del usuario
#         request.user.auth_token.delete()
#         return Response(status=status.HTTP_200_OK)


class UserRegistrationView(generics.CreateAPIView):
    """
    API endpoint to register a new user.
    """

    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class UserUpdateView(generics.UpdateAPIView):
    """
    API endpoint to update a user.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDeleteView(generics.DestroyAPIView):
    """
    API endpoint to delete a user.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDeactivateView(generics.UpdateAPIView):
    """
    API endpoint to deactivate a user.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
