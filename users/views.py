from rest_framework import status, viewsets, parsers
from django.contrib.auth.models import User
from rest_framework.response import Response
import json
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    parser_classes = [parsers.JSONParser]

    def create(self, request, format='json'):
        
        serializer = UserSerializer(data=json.loads(request.body), context={'request':request})
        if serializer.is_valid():
            user = serializer.save()
            if user:
                js = serializer.data
                return Response(js, status=status.HTTP_201_CREATED)
        #print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
