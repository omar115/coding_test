from django.urls import path
from .views import *

urlpatterns = [
    path('child/', ChildListApiView.as_view(), name="Child List"),
    path('book/', BookListApiView.as_view(), name="Book List"),
    path('author/', AuthorListApiView.as_view(), name="Author List"),
    path('book/update/<id>/', BookUpdateApiView.as_view(), name="update"),
]