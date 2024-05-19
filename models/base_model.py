#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
     def __init__(self):
         self.id = str(uuid.uuid4())
         self.created_at = datetime.now()
         self.updated_at = self.created_at

     def __str__(self):
         return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

     def save(self):
         self.updated_at = datetime.now()

     def to_dict(self):
         dict_container = self.__dict__.copy()
         dict_container['__class__'] = self.__class__.__name__
         dict_container['created_at'] = self.created_at.isoformat()
         dict_container['updated_at'] = self.updated_at.isoformat()
         return dict_container
