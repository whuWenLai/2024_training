### （一）项目结构

**1.downloadn_info.py**  下载数据并解压当前目录 

**2.data_clean_ceate_table.py** 对数据进行清洗，并将关联的文件按照要求读取解析等处理，创建data_info表

**3.data_model.py**  data_info表的映射类

**4.api_service.py** fastapi搭建的http api服务

### （二）结果展示
1.虚拟机中docker部署的mysql

![alt text](/图片/img.png)

2.http api服务
![alt text](/图片/http_api.png)
3.根据Image文件名查询，返回关联的 lidar/*.json的json数据、返回关联的calib/*/*.json数据，返回图片本地http地址
![img.png](/图片/query1.png)
![img.png](/图片/query2.png)
4.地址可以复制到浏览器下载
![img.png](/图片/image_url.png)