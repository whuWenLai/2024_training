import os
import pandas as pd
from sqlalchemy import create_engine

# 读取json文件
data = pd.read_json('./single-vehicle-side-example/data_info.json')

# 进行数据清洗操作，比如删除缺失值、重复值，格式化日期等
cleaned_data = data.dropna().drop_duplicates()
# - 对关联的文本文件，读取并解析之后，存储到上一个步骤的同一行数据表里面
# - 对关联的二进制文件，读取文件大小，存储到上一个步骤的同一行数据表里面
for index, row in cleaned_data.iterrows():
    for key, value in row.items():
        if key  in ('calib_camera_intrinsic_path','calib_lidar_to_camera_path','label_camera_std_path','label_lidar_std_path'):# 指定需要修改值的键
            # - 对关联的文本文件，读取并解析之后，存储到上一个步骤的同一行数据表里面
            with open(f'single-vehicle-side-example/{cleaned_data.at[index, key]}','r',encoding='UTF-8') as f:
                value = f.read()
            cleaned_data.at[index, key] = value
        if key == 'image_path':
            #加一个image_id字段 便于查询
            cleaned_data.at[index, 'image_id']=cleaned_data.at[index, key][6:12]
            cleaned_data.at[index, key]=f'http:localhost:8080/{cleaned_data.at[index, key]}'
        if key == 'pointcloud_path':
            #- 对关联的二进制文件，读取文件大小，存储到上一个步骤的同一行数据表里面
            filename = f'single-vehicle-side-example/{cleaned_data.at[index, key]}'
            file_size = os.path.getsize(filename)
            #单位kb
            file_size=file_size/1024
            cleaned_data.at[index, key]=f'{file_size:.2f}kb'


# 进行数据清洗操作，比如删除缺失值、重复值，格式化日期等
cleaned_data = cleaned_data.dropna().drop_duplicates()

#虚拟机上的数据库连接和建表操作：
engine = create_engine('mysql+mysqldb://root:root@192.168.150.101/DAIR', echo=True)
cleaned_data.to_sql('data_info', con=engine, if_exists='replace', index=False)