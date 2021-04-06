from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view()
# def hello_world(request):
#     return Response({'msg':'Hello world'})
#

# @api_view(['POST'])
# def hello_world(request):
#     print(request.data)
#     if request.method=="POST":
#      return Response({'msg':'This is POST mehtod'})
#


@api_view(['GET','POST'])
def hello_world(request):
    print(request.data)
    if request.method=='GET':
     return Response({'msg':'This is GET request','data':request.data})
    if request.method=="POST":
     print(request.data)
     return Response({'msg':'This is POST request','data':request.data})


