# models.py
from mongoengine import Document, StringField, ReferenceField, DateTimeField
from datetime import datetime

class User(Document):
    username = StringField(required=True, unique=True)#user
    password = StringField(required=True)#password

class Note(Document):
    title = StringField(required=True)#ชื่อเรื่อง
    content = StringField()#เนื้อหา
    created_at = DateTimeField(default=datetime.utcnow)#วันที่สร้าง
    user = ReferenceField(User)# class user
