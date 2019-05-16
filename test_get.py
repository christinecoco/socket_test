#coding=utf-8
import requests
import json
url="https://devopenapi.ywart.com/2.0/api/Artworks?keyword=李"

def build_uri():
    return '/'.join([url])#主要作用是拼接接口请求地址

def better_output(json_str):
    return json.dumps(json.loads(json_str),ensure_ascii=False,indent=4)#采用json里面提供方法打印出来，格式更好看

def request_method():
    response=requests.get(build_uri())#调用get方法
    print(better_output(response.text))#调用json更好格式输出

if __name__=='__main__':
    request_method()