import requests
from requests.auth import AuthBase

Base_URL='https://api.github.com'

def build_uri(endpoint):
    return '/'.join([Base_URL,endpoint])

class GithubAuth(AuthBase):

    def __init__(self,token):
        self.token=token

    def __call__(self, r):
        #给request添加headers
        r.headers['Authorization']=' '.join(['token',self.token])
        return r

def oauth_request_advance():
    auth=GithubAuth('35c02ac823ea31960c7a538c6727390fb1f082e2')
    response=requests.get(build_uri('user/emails'),auth=auth)
    print(response.text)

oauth_request_advance()