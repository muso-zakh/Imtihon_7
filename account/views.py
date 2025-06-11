from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .serializers import RegisterSerializer, Profile, ChangePasswordSerializer

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView


# Foydalanuvchini ro'yxatdan o'tkazish
@swagger_auto_schema(method='post', request_body=RegisterSerializer)
@api_view(['POST'])
def register_api(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Foydalanuvchi profilini ko'rsatish
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    serializer = Profile(request.user)
    return Response(serializer.data)

# Login qilish va token qaytarish
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id})

# Parolni o'zgartirish
@swagger_auto_schema(method='post', request_body=ChangePasswordSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    serializer = ChangePasswordSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    old_password = serializer.validated_data['old_password']
    new_password = serializer.validated_data['new_password']
    user = request.user

    if not user.check_password(old_password):
        return Response({"error": "Eski parol noto‘g‘ri"}, status=status.HTTP_400_BAD_REQUEST)

    # Yangi parolni validatsiya qilish
    try:
        validate_password(new_password, user=user)
    except ValidationError as e:
        return Response({"error": e.messages}, status=status.HTTP_400_BAD_REQUEST)

    user.set_password(new_password)
    user.save()

    return Response({"success": "Parol yangilandi"}, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"success": "Logout muvaffaqiyatli bajarildi"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)