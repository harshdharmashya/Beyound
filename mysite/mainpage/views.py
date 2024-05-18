from django.shortcuts import render
from django.http import JsonResponse
import json
import requests
# Create your views here.
def indexpage(request): 
    response=requests.get('https://devapi.beyondchats.com/api/get_message_with_sources').json()
    # print(response["data"]["data"])
    dataArray = []
    for i in response["data"]["data"]:
        # print(i['source'])
        m = []
        for j in i['source']:
            if(j['link']):
                k = {
                    'id': j['id'] ,
                    'link': j['link']
                }
                m.append(k)
        n={
            "id" : i['id'],
            "response" : i['response'],
            "source" : m
        }
        dataArray.append(n)

    return render(request,'index.htm',{'response':dataArray})
