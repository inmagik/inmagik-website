from rest_framework import serializers, viewsets, views
from rest_framework.response import Response
from django.contrib.auth import get_user_model

# Me
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')

class MeView(views.APIView):
    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
