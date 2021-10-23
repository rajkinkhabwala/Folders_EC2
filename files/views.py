from rest_framework import viewsets, parsers, permissions
from rest_framework.response import Response
from .models import Upload
from .serializers import FileSerializer

class FileViewSet(viewsets.ModelViewSet):
    permission_classes  = [permissions.AllowAny]
    serializer_class = FileSerializer
    queryset= Upload.objects.all()
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    # def get_queryset(self):
    #         user = self.request.user
    #         return Upload.objects.filter(user=user)