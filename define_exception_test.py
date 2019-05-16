import json
import requests
from requests import exceptions

url='https://api.github.com'

def build_uri(endpoint):
    return '/'.join([url,endpoint])

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def custom_request():
    from requests import Request,Session
    s=Session()
    headers={'User-Agent':'fake1.3.4'}
    request=Request('GET',build_uri('uesr/emails'),auth=('christinecoco','kk1330043088@163.com'),headers=headers)
    preped=request.prepare()
    print(preped.body)
    print(preped.headers)

    response=s.send(preped,timeout=5)
    print(response.status_code)
    print(response.headers)
    print(response.text)

if __name__=='__main__':
    custom_request()