from django.http import HttpResponse
import json

class HttpResponseMixin(object):
    def render_to_http_response(self,data,status=200):
        return HttpResponse(data,content_type='application/json',status=status)


class SerializeMixin(object):
    def serialize(self,qs):
        p_data=json.loads(json_data)
        final_list=[]
        for obj in p_data:
            std_data=obj['fields']
            final_list.append(std_data)
        json_data=json.dumps(final_list)
        return json_data
