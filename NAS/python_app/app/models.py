from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str
    
class UserCreate(UserBase):
    password: str
    
class User(UserBase):
    id: int
    created_at: datetime = datetime.now()
    
    class Config:
        orm_mode = True
        
class FileInfo(BaseModel):
    id: int
    filename: str
    size: int
    upload_date: datetime
    owner_id: int
    
    class Config:
        orm_mode = True
        
# Mock database for development purposes
mock_users = [
    {"id": 1, "username": "admin", "email": "admin@example.com", "password": "admin123"},
    {"id": 2, "username": "user", "email": "user@example.com", "password": "user123"}
]

mock_files = [
    {"id": 1, "filename": "document.pdf", "size": 1024000, "upload_date": datetime.now(), "owner_id": 1},
    {"id": 2, "filename": "image.jpg", "size": 512000, "upload_date": datetime.now(), "owner_id": 1},
    {"id": 3, "filename": "data.csv", "size": 256000, "upload_date": datetime.now(), "owner_id": 2},
    {"id": 4, "filename": "presentation.pptx", "size": 2048000, "upload_date": datetime.now(), "owner_id": 2},
    {"id": 5, "filename": "backup.zip", "size": 5120000, "upload_date": datetime.now(), "owner_id": 1}
] 