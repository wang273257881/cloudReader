# -*- coding:UTF-8 -*-
"""
Created on 2021年7月21日

@author: wwp
信息同步相关接口
"""
import os
import sys
sys.path.append('../../')
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from cloudReaderDb import schemas
from cloudReaderDb.database import SessionLocal, engine, Base
from cloudReaderDb.crud import crudAdmin

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




# 笔记信息同步
@router.post("/noteSynchronization/", response_model=schemas.NoteList)
async def get_key(item: schemas.NoteList, db: Session = Depends(get_db)):
    return None

# 书签信息同步
@router.post("/bookMarkSynchronization/", response_model=schemas.BookMarkList)
async def get_key(item: schemas.BookMarkList, db: Session = Depends(get_db)):
    return None