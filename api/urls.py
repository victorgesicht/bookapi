from django.urls import path
from . import views

urlpatterns=[
    path('books/', views.bookListCreate.as_view(), name="bookcreate"),
    path('books/<int:pk>/', views.bookListRetrieveUpdateDestroy.as_view(), name="bookupdatedelete")
    
]