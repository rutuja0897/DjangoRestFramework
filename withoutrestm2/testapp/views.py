from django.shortcuts import render
from django.views.generic import View
from testapp.utils import is_json
from testapp.mixins import SerializeMixin,HttpResponseMixin
from testapp.models import Student
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.forms import StudentForm


# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class StudentCRUDCBV(HttpResponseMixin,View):
    def get_object_by_id(self,id):
        try:
            s=Student.objects.get(id=id)
        except Student.DoesNotExist:
            s=None
        return s


    def get(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'Please provide valid json data only'}),status=400)
        pdata=json.loads(data)
        id=pdata.get('id',None)
        if id is not None:
            std=self.get_object_by_id(id)
            if std is None:
                return self.render_to_http_response(json.dumps({'msg':'No matched record found with matched id'}),status=400)
            json_data=self.serialize([std,])
            return self.render_to_http_response(json_data)
        qs=Student.objects.all()
        json_data=self.serialize(qs)
        return self.render_to_http_response(json_data)


    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'Please provide valid json data only'}),status=400)
        std_data=json.loads(data)
        form=StudentForm(std_data)
        if form.is_valid():
            form.save(commit=True)
            return self.render_to_http_response(json.dumps({'msg':'Resource created successfully'}))
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)



    def put(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'Please provide valid json data only'}),status=400)
        provided_data=json.loads(data)
        id=provided_data.get('id',None)
        if id is None:
            return self.render_to_http_response(json.dumps({'msg':'To perform updation id is mandatory plz provide'}),status=400)
        std=self.get_object_by_id(id)
        if std is None:
            return self.render_to_http_response(json.dumps({'msg': 'No matched id record found with the given id '}),status=400)
        original_data={
        'name':std.name,
        'rollno':std.rollno,
        'marks':std.marks,
        'gf':std.gf,
        'bf':std.bf,
        }
        original_data.update(provided_data)
        form=StudentForm(original_data,instance=std)
        if form.is_valid():
            form.save(commit=True)
            return self.render_to_http_response(json.dumps({'msg': 'Resource updated successfully '}),status=400)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def delete(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please send valid json data only'})
            return self.render_to_http_response(json_data, status=400)
        pdata = json.loads(data)
        id = pdata.get('id', None)
        if id is not None:
            std = self.get_object_by_id(id)
            if std is None:
                json_data = json.dumps({'msg': 'The requested resource not available with matchedid'})
                return self.render_to_http_respnse(json_data, status=404)
            status, deleted_item = std.delete()
            if status == 1:
                json_data = json.dumps({'msg': 'Resource deleted successfully'})
                return self.render_to_http_respnse(json_data)
            json_data = json.dumps({'msg': 'Unable to delete......plz try again'})
            return self.render_to_http_respnse(json_data)
        json_data = json.dumps({'msg': 'TO perform deletion id is mandatory,please provide'})
        return self.render_to_http_respnse(json_data, status=400)
