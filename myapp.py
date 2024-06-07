import requests
import json
URL="http://127.0.0.1:8000/studentinfo/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.get(url=URL,headers=headers, data=json_data)
    data=r.json()

get_data()

def post(request):
    data={
        'name':'shakil',
        'roll':101,
        'city':'dhaka',
    }
    headers={'content-Type':'application/json'}
    if id is not None:
        data={'id':id}
        json_data=json.dumps(data)
        r=requests.post(url=URL,headers=headers,data=json_data)
        data=r.json()

post()

def Update(request):
    data={
        'id':3,
        'name':'shakil',
        'city':'dhaka',
    }
    headers={'content-Type':'application/json'}
    if id is not None:
        data={'id':id}
        json_data=json.dumps(data)
        r=requests.put(url=URL,headers=headers,data=json_data)
        data=r.json()

Update()


def deleted_Data(request):
    data={
        'id':3}
    hearders={'content-Type':'application/json'}
    if id is not None:
        data={'id':id}
        json_data=json.dumps(data)
        r=requests.delete(url=URL,headers=hearders,data=json_data)
        data=r.json()

deleted_Data()



