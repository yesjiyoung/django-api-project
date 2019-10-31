# viewSet 바탕으로 작성할거야.
from rest_framework import viewsets
from .models import Essay, Album, Files
from .serializers import EssaySerializer, AlbumSerializer, FilesSerializer
from rest_framework.filters import SearchFilter #기본 내장 라이브러리 써서 Search 기능 구현하자

from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.response import Response
from rest_framework import status

class PostViewSet(viewsets.ModelViewSet):
    
    queryset = Essay.objects.all() # queryset을 위해서 model필요
    serializer_class = EssaySerializer # serializer 필요

    filter_backends=[SearchFilter]
    search_fields=('title','body')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user) 

    # 현재 request를 보낸 유저
    # == self.request.user
    # 음? user 기반으로 queryset을 필터링 한다?
    def get_queryset(self):
        qs = super().get_queryset()
        
        # 부모의 super()의 queryset을 다 갖고와서 지지고볶고하기
        if self.request.user.is_authenticated:
            qs=qs.filter(author=self.request.user)
        # 추가해볼 것) else if admin은 다 볼 수 있게?
        else:
            qs = qs.none()
        return qs

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all() # queryset을 위해서 model필요
    serializer_class = AlbumSerializer # serializer 필요

class FileViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all() # queryset을 위해서 model필요
    serializer_class = FilesSerializer # serializer 필요

    # parser_class 지정
    parser_classes=(MultiPartParser, FormParser) # 다양한 종류의 파일들을 수락할 수 있도록 형식들을 포함시켜주는거야.

    # create() 오버라이딩
    # API HTTP 메소드에 따라서 오버라이딩 시켰자나 get() post()이런거를!! 전에!
    # create() --> post() / API시간에 했던거랑 같아용
    def post(self, request, *args, **kwargs):
        # 파일 요청할 수 있도록 커스터마이징 할거야.
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.error, status=HTTP_400_BAD_REQUEST)
    
