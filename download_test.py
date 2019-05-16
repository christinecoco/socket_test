import requests

def download_image():
    url='http://img4.imgtn.bdimg.com/it/u=36529606,3560827590&fm=26&gp=0.jpg'

    response=requests.get(url)
    print(response.status_code)
    print(response.content)

if __name__=='__main__':
    download_image()