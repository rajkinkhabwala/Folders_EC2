from django.db import models
from django.contrib.auth.models import User

class Upload(models.Model):
    name = models.CharField(max_length=60)
    object = models.FileField(upload_to='files/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=1, related_name="user")

    class Meta:
        verbose_name = 'Upload'
        verbose_name_plural = 'Uploads'