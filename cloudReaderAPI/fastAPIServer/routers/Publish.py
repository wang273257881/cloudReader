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




# 添加新内容
@router.post("/addContent/", response_model=schemas.ContentCatalogList)
async def add_content(item: schemas.ContentCatalogList, db: Session = Depends(get_db)):
    return crudAdmin.db_create_contentcataloglist(db=db, contentcataloglist=item)

# 添加新交易
@router.post("/addTx/", response_model=schemas.ContentUseTransaction)
async def add_tx(item: schemas.ContentUseTransaction, db: Session = Depends(get_db)):
    return crudAdmin.db_create_contentusetransaction(db=db, contentusetransaction=item)

# 添加新内容存储
@router.post("/addLocation/", response_model=schemas.ContentObjectLocation)
async def add_location(item: schemas.ContentObjectLocation, db: Session = Depends(get_db)):
    return crudAdmin.db_create_contentobjectlocation(db=db, contentobjectlocation=item)

# 获取当前网络中的结点列表信息
@router.get("/getNodeList", response_model=List[schemas.NodeInformation])
async def get_node_list(db: Session = Depends(get_db)):
    db_user = crudAdmin.get_node_list(db)
    if not db_user:
        raise HTTPException(status_code=404, detail="Nids not found")
    return db_user