from django.shortcuts import render
from rest_framework import generics
from .serializer import bookSerializer
from .models import book

# Create your views here.
class bookListCreate(generics.ListCreateAPIView):
    queryset=book.objects.all()
    serializer_class=bookSerializer
    

class bookListRetrieveUpdateDestroy(generics.RetrieveDestroyAPIView):
    queryset=book.objects.all()
    serializer_class=bookSerializer
    lookup_field="pk"