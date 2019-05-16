import json
import requests

url='https://api.github.com'

def build_uri(endpoint):
    return '/'.join([url,endpoint])

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_method():
    response=requests.delete(build_uri('user/emails'),auth=('kk1330043088@163.com','HAN158xiao932'),json=['kk1330043088@163.com'])
    print(response.request.headers)
    print(response.request.body)

if __name__=='__main__':
    request_method()