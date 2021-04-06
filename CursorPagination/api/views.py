from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .Mypagination import MyCursorPagination

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class = [MyCursorPagination]
