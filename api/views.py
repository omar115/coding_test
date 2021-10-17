from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from .models import *
from .serializers import *

# Create your views here.

class ChildListApiView(ListAPIView):
    queryset = ChildUserModel.objects.all()
    serializer_class = ChildUserModelSerializer

class BookListApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorListApiView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorCreateApiView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
