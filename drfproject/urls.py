
from django.contrib import admin
from django.urls import path, include
from mystorage import urls
from rest_framework import urls # 로그인기능 구현
from django.conf import settings # 미디어 파일 url관련
from django.conf.urls.static import static # 미디어 파일 url관련

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mystorage.urls')),
    path('api-auth/', include('rest_framework.urls')) # 로그인기능 구현
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)