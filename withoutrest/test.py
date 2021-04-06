import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='apijsoncbv'
#resp=requests.get(BASE_URL+ENDPOINT)
resp=requests.post(BASE_URL+ENDPOINT)
#resp=requests.put(BASE_URL+ENDPOINT)
#resp=requests.delete(BASE_URL+ENDPOINT)
#print(resp.json())
data=resp.json()
print(data)
