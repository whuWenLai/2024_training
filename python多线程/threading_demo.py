
import threading
import requests

#定义获取的url的地址和headers
url='https://www.baidu.com'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}
#保存数据的文件
file=open('test.txt','wb')

#定义获取和下载网页内容的函数
def download_data(url):
    r = requests.get(url,headers = headers)
    if r.status_code == 200:
        file.write(r.content)


threads=[]
#创建五个线程执行任务
for i in range(5):
    t = threading.Thread(target=download_data, args=(url,))
    threads.append(t)
    t.start()

#所有线程执行完成
for t in threads:
    t.join()

file.close()


