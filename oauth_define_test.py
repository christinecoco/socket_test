import requests

Base_URL='https://api.github.com'

def build_uri(end_point):
    return '/'.join([Base_URL,end_point])

def oauth_auth():

    headers={'Authorization':'token  35c02ac823ea31960c7a538c6727390fb1f082e2'}
    #获取user/email信息
    response=requests.get(build_uri('user/emails'),headers=headers)

    print(response.status_code)
    print(response.text)
    print(response.request.headers)

oauth_auth()