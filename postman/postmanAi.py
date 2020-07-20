import json
import requests

def readJson():
    return json.load(open('one.json','r'))


def one_get():
    requests.session()
    print(dir(requests))
    res= requests.request(method=readJson()['requests'][0]['method'],url=readJson()['requests'][0]['url'])
    print(res.json())


one_get()



