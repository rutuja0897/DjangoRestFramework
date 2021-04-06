from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView



class ListCreateStudent(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class RetriveUpdateDestroyStudent(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
