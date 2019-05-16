import requests
from contextlib import closing

def download_image():
    url='http://img4.imgtn.bdimg.com/it/u=36529606,3560827590&fm=26&gp=0.jpg'

    response=requests.get(url,stream=True)

    with closing(requests.get(url,stream=True)) as response:
        #这里打开一个空的png文件，相当于创建一个空的txt文件，wb表示写文件
        with open('selenium.png','wb')as file:
            #每128个流遍历一次
            for data in response.iter_content(128):
                #把流写入到文件，这个文件最后写入完成就是，selenium.png
                file.write(data)

    print(response.status_code)

if __name__=='__main__':
    download_image()