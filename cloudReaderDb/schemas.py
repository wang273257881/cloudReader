# -*- coding:UTF-8 -*-
"""
Created on 2021年7月20日

@author: wwp
模型验证
"""
import os
import sys
from typing import List
sys.path.append(os.pardir)
from pydantic import BaseModel
import datetime

class ContentCatalogList(BaseModel):
    cid: str
    uid: str
    pid: str
    author: str
    title: str
    description: str
    publisher: str
    publishid: str
    isencrypt: int
    size: float
    content_hash: str
    state: int
    createdAt: datetime.datetime
    updatedAt: datetime.datetime

    class Config:
        orm_mode = True

class UserModel(BaseModel):
    email: str
    password: str

class UserKey(BaseModel):
    user_id: int
    public_key: str
    private_key: str

class ResourceHold(BaseModel):
    user_id: int
    resource_id: int

class NoteItem(BaseModel):
    id: int
    address: str
    content: str
    createAt: datetime.datetime

class NoteList(BaseModel):
    user_id: int
    publisher_content_id: int
    note_list: List[NoteItem] = []

class BookMarkItem(BaseModel):
    id: int
    address: str
    createAt: datetime.datetime

class BookMarkList(BaseModel):
    user_id: int
    publisher_content_id: int
    book_mark_list: List[BookMarkItem] = []
