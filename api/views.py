from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateAPIView, UpdateAPIView
from .models import ParentUser, ChildUser
from .serializers import ParentUserModelSerializer, ChildUserModelSerializer
from rest_framework.response import Response


# Parent Views (List)
class ParentListApiView(ListAPIView):
    queryset = ParentUser.objects.all()
    serializer_class = ParentUserModelSerializer


# Parent Views for Creating 
class ParentCreateApiView(CreateAPIView):
    queryset = ParentUser.objects.all()
    serializer_class = ParentUserModelSerializer
    

# Api view for delete parent user
class ParentDestroyApiView(DestroyAPIView):
    queryset = ParentUser.objects.all()
    serializer_class = ParentUserModelSerializer
    lookup_field = 'id'

# update view for parent user 
class ParentUpdateApiView(UpdateAPIView):
    queryset = ParentUser.objects.all()
    serializer_class = ParentUserModelSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)


# list view for child user
class ChildListApiView(ListAPIView):
    queryset = ChildUser.objects.all()
    serializer_class = ChildUserModelSerializer

# create view for child user
class ChildCreateApiView(CreateAPIView):
    queryset = ChildUser.objects.all()
    serializer_class = ChildUserModelSerializer

# delete view for child user
class ChildDeleteApiView(DestroyAPIView):
    queryset = ChildUser.objects.all()
    serializer_class = ChildUserModelSerializer
    lookup_field = 'id'

# update view for child user
class ChildUpdateApiView(RetrieveUpdateAPIView):
    queryset = ChildUser.objects.all()
    serializer_class = ChildUserModelSerializer
    lookup_field = 'id'
