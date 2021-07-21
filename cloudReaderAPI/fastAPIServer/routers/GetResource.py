# -*- coding:UTF-8 -*-
"""
Created on 2021年7月18日

@author: Wzj
发布接口
"""
import os
import sys
sys.path.append('../../')
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from contentDb import schemas
from contentDb.database import SessionLocal, engine, Base
from contentDb.crud import crudAdmin

Base.metadata.create_all(bind=engine) #数据库初始化，如果没有库或者表，会自动创建

router = APIRouter(
    tags=["admin"],
    responses={404: {"description": "Not found"}},
)
# Dependency
def get_db():
    """
    每一个请求处理完毕后会关闭当前连接，不同的请求使用不同的连接
    :return:
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# 登录
@router.post("/login/", response_model=schemas.NodeInformation)
async def add_node(item: schemas.NodeInformation, db: Session = Depends(get_db)):
    return crudAdmin.db_create_nodeinformation(db=db, nodeinformation=item)
