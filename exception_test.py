import json
import requests
from requests import exceptions

url='https://api.github.com'

def build_uri(endpoint):
    return '/'.join([url,endpoint])

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def timeout_request():
    try:
        response=requests.get(build_uri('user/emails'),auth=('christinecoco','HAN158xiao932'),timeout=10)
    except exceptions.Timeout as e:
        print(str(e))
    else:
        print(response.text)

if __name__=='__main__':
    timeout_request()