from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import UserRegisterationSerializer
from rest_framework.response import Response
from rest_framework import status

class UserRegisterView(APIView):
    # Because this is a registeration form and allowed for all
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        reg_serializer = UserRegisterationSerializer(data =request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
