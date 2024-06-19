from sqlalchemy import create_engine, String,Text, BigInteger, JSON, Column
from sqlalchemy.ext.declarative import declarative_base

from 第四周大作业.data_clean_create_table import engine

Base = declarative_base()

# Define database models
class Data_info(Base):
    __tablename__ = "data_info"

    image_id = Column(String(6), primary_key=True)
    image_path = Column(String(255))
    image_timestamp = Column(BigInteger)
    pointcloud_path = Column(Text)
    point_cloud_stamp = Column(BigInteger)
    calib_camera_intrinsic_path = Column(JSON)
    calib_lidar_to_camera_path = Column(JSON)
    label_camera_std_path = Column(JSON)
    label_lidar_std_path = Column(JSON)


Base.metadata.create_all(engine)