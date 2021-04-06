from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views.generic import View
from testapp.mixin import HttpResponseMixin


# Create your views here.

# def emp_data_jsonview2(request):
# emp_data={
##'ename':'Sunny',
# 'esal':1000,
# 'eaddr':'Mumbai',
# }
# resp='Employee Number:{}<br> Employee Name:{}<br> Employee Salary:{} <br>Employee Address:{}<br>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
# return HttpResponse(resp)
# json_data=json.dumps(emp_data)
# return HttpResponse(json_data,content_type='application/json')
# return JsonResponse(emp_data)

# class JsonCBV(View):
# def get(self,request,*args,**kwargs):
# emp_data={
# 'eno':100,
# 'ename':'Sunny',
## 'eaddr':'Mumbai',
# }
# return JsonResponse(emp_data)

#class JsonCBV(View):
   # def get(self, request, *args, **kwargs):
       #json_data = json.dumps({'msg': 'This is from get method'})
      # return HttpResponse(json_data,content_type='application/json')

    #def post(self, request, *args, **kwargs):
        #json_data = json.dumps({'msg': 'This is from post method'})
        #return HttpResponse(json_data, content_type='application/json')

   # def put(self, request, *args, **kwargs):
        #json_data = json.dumps({'msg': 'This is from put method'})
        #return HttpResponse(json_data, content_type='application/json')

    #def delete(self, request, *args, **kwargs):
       # json_data = json.dumps({'msg': 'This is from delete method'})
        #return HttpResponse(json_data, content_type='application/json')

class JsonCBV(HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This is from get method'})
        return render_to_http_response(json_data)



