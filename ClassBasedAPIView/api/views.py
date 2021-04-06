from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

# Create your views here.
class StudentAPI(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
         stu=Student.objects.get(pk=id)
         serializer=StudentSerializer(stu)
         return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'})
        return Response(serializer.error)

    def put(self,request,pk,format=None):
        id=pk
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete data updated'})
        return Response(serializer.error)

    def patch(self,request,pk,format=None):
        id = pk
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'partial data updated'})
        return Response(serializer.error)

    def delete(self,request,pk,format=None):
        id = pk
        stu = Student.object.get(id=id)
        stu.delete()
        return Response({'msg': 'Data deleted'})









