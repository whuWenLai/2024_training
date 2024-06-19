import os
from contextlib import contextmanager
import uvicorn
from fastapi import FastAPI, Path, Query, Body, Cookie, Header, Request, Response, HTTPException, status, Depends
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column, scoped_session
from starlette.responses import FileResponse

from 第四周大作业.data_clean_create_table import engine
from 第四周大作业.data_model import Data_info


app = FastAPI()

#根据image文件名查询，获取相关联的json数据,返回图片本地http地址
@app.get('/data_info/{image_id}')
async def get_data_info(image_id: str):
    with session_scope() as session:
        image_id = image_id[0:6]
        data = session.query(Data_info).filter(Data_info.image_id == image_id).first()

        response ={
            "image_url" : data.image_path,
            "calib_camera_intrinsic_info":data.calib_camera_intrinsic_path,
            "calib_lidar_to_camera_info":data.label_camera_std_path,
            "label_lidar_std_info":data.label_lidar_std_path,
            "label_camera_std_info":data.label_camera_std_path
        }

        return response

#根据图片本地http地址获取图片
@app.get("/image/{image_name}/")
async def get_image(image_name: str):
    image_path = f'single-vehicle-side-example/image/{image_name}'
    print(image_path)
    if not os.path.exists(image_path):
        return {"error": "Image not found"}

    return FileResponse(image_path)





session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
@contextmanager
def session_scope():

    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
        raise
    finally:
        session.close()



if __name__ == '__main__':
    uvicorn.run("api_service:app",port=8080, reload=True)