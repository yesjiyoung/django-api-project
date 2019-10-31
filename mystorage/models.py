from django.db import models
from django.conf import settings

# Create your models here.
class Essay(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE) 
    #on_delete : 게시물지우면 모델도 같이 지워진다.
    title = models.CharField(max_length=30)
    body = models.TextField()

# 사용자들이 직접 업로드 할 수 있는 사진과 파일을 다루는 모델을 올려줄거야!!

class Album(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to ="images")
    desc = models.CharField(max_length=100)
class Files(models.Model):
    author= models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE) 
    myfile=models.FileField(blank=False, null=False, upload_to="files")
    desc=models.CharField(max_length=100)