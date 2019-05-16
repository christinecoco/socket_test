import requests

Base_Url='https://api.github.com'

def build_uri(end_point):
    return '/'.join([Base_Url,end_point])

def basic_auth():
    response=requests.get(build_uri('user'),auth=('christinecoco','HAN158xiao932'))
    print(response.status_code)
    print(response.text)
    print(response.request.headers)

basic_auth()