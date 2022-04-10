from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from firebase_admin import auth
from django.contrib.auth import get_user_model


class CheckIfAuthenticated(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({'message': 'authentication succeeded'})


class Register(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        User = get_user_model()
        user = User.objects.get(username=request.user.username)
        firebase_user_data = auth.get_user(user.username)
        user.email = firebase_user_data.email
        user.save()
        return Response({'message': 'user registered successfully'})
