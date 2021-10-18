from django.urls import path
from .views import *

urlpatterns = [
    path('child/', ChildListApiView.as_view(), name="child-user-list"),
    path('parent/', ParentListApiView.as_view(), name="parent-user-list"),
    path('parent/create/', ParentCreateApiView.as_view(), name="parent-user-create"),
    path('parent/delete/<id>/', ParentDestroyApiView.as_view(), name="parent-user-delete"),
    path('parent/update/<id>/', ParentUpdateApiView.as_view(), name="parent-user-update"),
    path('child/create/', ChildCreateApiView.as_view(), name="child-user-create"),
    path('child/delete/<id>/', ChildDeleteApiView.as_view(), name="child-user-delete"),
    path('child/update/<id>/', ChildUpdateApiView.as_view(), name="child-user-update"),
    
]