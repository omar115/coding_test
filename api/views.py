from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.parsers import FormParser, MultiPartParser
from .models import *
from .serializers import *
from rest_framework.response import Response

from rest_framework.exceptions import (
    PermissionDenied, NotFound, NotAuthenticated, MethodNotAllowed
)
# Create your views here.

class ParentListApiView(ListAPIView):
    queryset = ParentUser.objects.all()
    serializer_class = ParentUserModelSerializer


class ParentCreateApiView(CreateAPIView):
    queryset = ParentUser.objects.all()
    serializer_class = ParentUserModelSerializer
    

class ParentDestroyApiView(DestroyAPIView):
    queryset = ParentUser.objects.all()
    serializer_class = ParentUserModelSerializer
    lookup_field = 'id'

class ParentUpdateApiView(UpdateAPIView):
    queryset = ParentUser.objects.all()
    serializer_class = ParentUserModelSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)



class ChildListApiView(ListAPIView):
    queryset = ChildUser.objects.all()
    serializer_class = ChildUserModelSerializer

class ChildCreateApiView(CreateAPIView):
    queryset = ChildUser.objects.all()
    serializer_class = ChildUserModelSerializer

class ChildDeleteApiView(DestroyAPIView):
    queryset = ChildUser.objects.all()
    serializer_class = ChildUserModelSerializer
    lookup_field = 'id'

class ChildUpdateApiView(RetrieveUpdateAPIView):
    queryset = ChildUser.objects.all()
    serializer_class = ChildUserModelSerializer
    lookup_field = 'id'
