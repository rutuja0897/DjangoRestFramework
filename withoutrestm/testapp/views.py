from django.shortcuts import render
from testapp.models import Employee
from django.views.generic import View
import json
from django.http import HttpResponse
#from django.core.serializers import serialize
from testapp.mixin import SerializeMixin,HttpResponseMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.utils import is_json
from testapp.forms import EmployeeForm

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self,id):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp=None
        return emp
    def get(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only'})
            return self.render_to_http_response(json_data,status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            emp=self.get_object_by_id(id)
            if emp is None:
                json_data=json.dumps({'msg':'The requested resource not available with matched id '})
                return self.render_to_http_response(json_data, status=400)
            json_data=self.serialize([emp,])
            return self.render_to_http_response(json_data)
        qs=Employee.objects.all()
        json_data=self.serialize(qs)
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
         #json_data=json.dumps({'msg':'This is from post method'})
         #return self.render_to_http_response(json_data)
         data=request.body
         valid_json=is_json(data)
         if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only'})
            return self .render_to_http_response(json_data,status=400)
         emp_data=json.loads(data)
         form=EmployeeForm(emp_data)
         if form.is_valid():
             form.save(commit=True)
             json_data=json.dumps({'msg':'resource created successfully'})
             return self.render_to_http_response(json_data)
         if form.errors:
              json_data=json.dumps(form.errors)
              return self.render_to_http_response(json_data,status=400)




    def delete(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only'})
            return self.render_to_http_response(json_data,status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            emp=self.get_object_by_id(id)
            if emp is None:
                json_data=json.dumps({'msg':'The requested resource not available with matchedid'})
                return self.render_to_http_respnse(json_data,status=404)
            status,deleted_item=emp.delete()
            if status==1:
                json_data=json.dumps({'msg':'Resource deleted successfully'})
                return self.render_to_http_respnse(json_data)
            json_data = json.dumps({'msg': 'Unable to delete......plz try again'})
            return self.render_to_http_respnse(json_data)
        json_data = json.dumps({'msg': 'TO perform deletion id is mandatory,please provide'})
        return self.render_to_http_respnse(json_data,status=400)
# @method_decorator(csrf_exempt,name='dispatch')
# class EmployeeDetailCBV(HttpResponseMixin,SerializeMixin,View):
#     def get_object_by_id(self, id):
#         try:
#             emp = Employee.objects.get(id=id)
#         except Employee.DoesNotExist:
#             emp = None
#         return emp
#     def get(self,request,id,*args,**kwargs):
#         try:
#             emp=Employee.objects.get(id=id)
#         #emp=get_object_or_404(Employee,id=1)
#         except Employee.DoesNotExist:
#             json_data=json.dumps({'msg':'The requested resource not available'})        #json_data=json.dumps(emp_data
#             return self.render_to_http_response(json_data,status=404)
#         else:
#             json_data=self.serialize([emp,])
#             return self.render_to_http_response(json_data)
#
#         def put(self,request,id,*args,**kwargs):
#             emp=self.get_objects_by_id(id)
#             if emp is None:
#                 json_data=json.dumps({'msg':'No matched resource found,Not possible to perform updation.'})
#                 return self.render_to_http_response(json_data,status=404)
#             data=request.body
#             valid_json=is_json(data)
#             if not valid_json:
#                 json_data=json.dumps({'msg':'Please send valid json data only'})
#                 return self.render_to_http_response(json_data,status=400)
#             provided_data=json.loads(data)
#             original_data={
#                 'eno':emp.eno,
#                 'ename':emp.ename,
#                 'esal':emp.esal,
#                 'eaddr':emp.eaddr,
#             }
#             original_data.update(provided_data)
#             form=EmployeeForm(original_data,instance=emp)
#             if form.is_valid():
#                 form.save(commit=True)
#                 json_data=json.dumps({'msg':'Resource created successfully'})
#                 return self.render_to_http_response(json_data)
#             if form.errors:
#                 json_data=json.dumps(form.errors)
#                 return self.render_to_http_response(json_data,status=400)
#
#         def delete(self,request,id,*args,**kwargs):
#             emp=self.get_object_by_id(id)
#             if emp is None:
#                 json_data=json.dumps({'msg':'No matched resource found,not possible to perform deletion'})
#             return self.render_to_http_response(json_data,status=404)
#             status,deleted_item=emp.delete()
#             if status==1:
#                json_data=json.dumps({'msg':'Resource deleted successfully'})
#                return self.render_to_http_response(json_data)
#
#             json_data=json.dumps({'msg':'unable to delete.....plz try again'})
#             return self.render_to_http_response(json_data)

# @method_decorator(csrf_exempt,name='dispatch')
# class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
#     def get(self,request,*args,**kwargs):
#         qs=Employee.objects.all()
#         json_data=self.serialize(qs)
#         return HttpResponse(json_data,content_type='application/json')
#
#
#     def post(self,request,*args,**kwargs):
#         #json_data=json.dumps({'msg':'This is from post method'})
#         #return self.render_to_http_response(json_data)
#         data=request.body
#         valid_json=is_json(data)
#         if not valid_json:
#            json_data=json.dumps({'msg':'Please send valid json data only'})
#            return self .render_to_http_response(json_data,status=400)
#         emp_data=json.loads(data)
#         form=EmployeeForm(emp_data)
#         if form.is_valid():
#             form.save(commit=True)
#             json_data=json.dumps({'msg':'resource created successfully'})
#             return self.render_to_http_response(json_data)
#         if form.errors:
#              json_data=json.dumps(form.errors)
#              return self.render_to_http_response(json_data,status=400)