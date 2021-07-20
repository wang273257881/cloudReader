# -*- coding:UTF-8 -*-
"""
Created on 2021年7月20日

@author: wwp
数据库模型表
"""
import os
import sys
sys.path.append(os.pardir)
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.sql.sqltypes import DateTime, Float
from cloudReaderDb.database import Base


class User(Base):
    __tablename__ = "User"
    user_id = Column(Integer, primary_key=True, index=True, nullable=False)
    user_name = Column(String(255), default=None, nullable=False)
    identity = Column(Integer, default=None, nullable=False)
    password = Column(String(255), default=None, nullable=False)
    email = Column(String(255), default=None, nullable=False)

class UserSecretKey(Base):
    __tablename__ = "UserSecretKey"
    user_id = Column(Integer, primary_key=True, index=True, nullable=False)
    private_key = Column(String(255), default=None, nullable=False)
    public_key = Column(String(255), default=None, nullable=False)

class ContentInformetion(Base):
    __tablename__ = "ContentInformetion"
    publisher_content_id = Column(Integer, primary_key=True, index=True, nullable=False)
    author = Column(String(255), default=None, nullable=False)
    title = Column(String(255), default=None, nullable=False)
    description = Column(String(255), default=None)
    size = Column(Float, default=None, nullable=False)
    state = Column(Integer, default=None, nullable=False)
    createdAt = Column(DateTime, nullable=False)
    updatedAt = Column(DateTime, default=None)
    url = Column(String(255), default=None, nullable=False)

class ResourceHold(Base):
    __tablename__ = "ResourceHold"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    user_id = Column(Integer, default=None, nullable=False)
    resource_id = Column(Integer, default=None, nullable=False)

class ResourcePublish(Base):
    __tablename__ = "ResourcePublish"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    publisher_id = Column(Integer, default=None, nullable=False)
    resource_id = Column(Integer, default=None, nullable=False)
    is_encrypted = Column(Boolean, default=None, nullable=False)
    publisher_type = Column(Integer, default=None, nullable=False)
    publish_time = Column(DateTime, nullable=False)

class Note(Base):
    __tablename__ = "Note"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    user_id = Column(Integer, default=None, nullable=False)
    publisher_content_id = Column(Integer, default=None, nullable=False)
    address = Column(String(255), default=None, nullable=False)
    content = Column(String(255), default=None, nullable=False)
    createAt = Column(DateTime, nullable=False)

class BookMark(Base):
    __tablename__ = "BookMark"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    user_id = Column(Integer, default=None, nullable=False)
    publisher_content_id = Column(Integer, default=None, nullable=False)
    address = Column(String(255), default=None, nullable=False)
    createAt = Column(DateTime, nullable=False)
