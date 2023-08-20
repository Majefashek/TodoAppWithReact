from django.shortcuts import render
from django.views import View
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import generics

class ListTodo(generics.ListAPIView):
    queryset=Todo.objects.all()
    serializer_class = TodoSerializer

    pass

class DetailTodo(generics.RetrieveAPIView):
    queryset=Todo.objects.all()
    serializer_class = TodoSerializer
    pass
