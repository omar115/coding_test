from django.urls import path
from .views import *

urlpatterns = [
    path('child/', ChildListApiView.as_view(), name="Child List"),
    path('parent/', ParentListApiView.as_view(), name="Parent List"),
    path('child/<id>/', ChildRetrieveApiView.as_view(), name="Single Child Data"),
    path('child_update/<id>/', ChildUpdateApiView.as_view(), name="Single Child Update"),
    
    # path('author/', AuthorListApiView.as_view(), name="Author List"),
    # path('book/update/<id>/', BookUpdateApiView.as_view(), name="update"),
]