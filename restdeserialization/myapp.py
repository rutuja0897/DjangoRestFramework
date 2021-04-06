import requests
import json
URL='http://127.0.0.1:8000/stucreate/'
data={
    'name':'sonam',
    'roll':101,
    'city':'Pune',
}
json_data=json.dumps(data)
r=requests.post(url=URL,data=json_data)
data=r.json()
print(data)
# BASE_URL = 'http://127.0.0.1:8000/'
# ENDPOINT = 'stucreate/'
# data={
#     'name':'sonam',
#     'roll':101,
#     'city':'Pune'
# }
# resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(data))
# print(resp.status_code)
# print(resp.json())
