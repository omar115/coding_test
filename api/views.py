from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, RetrieveUpdateAPIView, UpdateAPIView
from .models import *
from .serializers import *

# Create your views here.

class ParentListApiView(ListAPIView):
    queryset = ParentUser.objects.all()
    serializer_class = ParentUserModelSerializer


class ParentRetrieveApiView(RetrieveAPIView):
    queryset = ParentUser.objects.all()
    serializer_class = ParentUserModelSerializer
    lookup_field = 'id'

class ParentUpdateApiView(UpdateAPIView):
    queryset = ParentUser.objects.all()
    serializer_class = ParentUserModelSerializer
    lookup_field = 'id'

class ParentDestroyApiView(DestroyAPIView):
    queryset = ParentUser.objects.all()
    serializer_class = ParentUserModelSerializer
    lookup_field = 'id'

class ChildListApiView(ListAPIView):
    queryset = ChildUser.objects.all()
    serializer_class = ChildUserModelSerializer

class ChildRetrieveApiView(RetrieveAPIView):
    queryset = ChildUser.objects.all()
    serializer_class = ChildUserModelSerializer
    lookup_field = 'id'


class ChildUpdateApiView(RetrieveUpdateAPIView):
    queryset = ChildUser.objects.all()
    serializer_class = ChildUserModelSerializer
    lookup_field = 'id'


# class ChildListApiView(ListAPIView):
#     queryset = ChildUserModel.objects.all()
#     serializer_class = ChildUserModelSerializer

# class BookListApiView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class AuthorListApiView(ListAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# class AuthorCreateApiView(CreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# class BookUpdateApiView(UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field='id'
