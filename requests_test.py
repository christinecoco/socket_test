import requests

# 请求百度网页
response = requests.get("https://www.ywart.com", data=None, timeout=10)
print(response.headers)
