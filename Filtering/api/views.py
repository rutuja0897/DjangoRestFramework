from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student

# Create your views here.
class StudentList(ListAPIView):
    #queryset =  Student.objects.filter(passby='User2')
    serializer_class=StudentSerializer
    def get_queryset(self):#user Login karega us tym hi data dikhega
        user=self.request.user
        return Student.objects.filter(passby=user)
