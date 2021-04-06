import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'api/'
def create_resource():
    new_std = {
        'name':'Dhoni',
        'rollno':105,
        'marks':35,
        'gf':'Sakshi',
        'bf':'Raj',
    }
    resp = requests.post(BASE_URL + ENDPOINT,data=json.dumps(new_std))
    print(resp.status_code)
    print(resp.json())
create_resource()
