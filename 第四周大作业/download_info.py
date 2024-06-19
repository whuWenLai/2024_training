import tempfile
import zipfile
import requests
from sqlalchemy import create_engine

#下载数据
url = "https://bj.bcebos.com/apollo-air/v2-2022-01-08/single-vehicle-side-example_16214245417164800.zip?authorization=bce-auth-v1%2F62ff93831d5840338d0fcc9585430b3a%2F2024-06-18T10%3A49%3A14Z%2F604800%2F%2Fa27475e837306c91c249dc66365b6a449e2ebf73fc86af972ba1992b80c1723f"
response = requests.get(url)
data = response.content
_tmp_file = tempfile.TemporaryFile()  # 创建临时文件
print(_tmp_file)

_tmp_file.write(data)  # byte字节数据写入临时文件
# _tmp_file.seek(0)

zf = zipfile.ZipFile(_tmp_file, mode='r')
for names in zf.namelist():
    f = zf.extract(names, './')  # 解压到zip目录文件下
    print(f)
