from pymongo import MongoClient
# import asyncio
from app.settings import settings


class MongoDB:
    def __init__(self):
        # self.URL=f"mongodb+srv://{settings.DATABASEUSER}:{settings.DATABASEPASSWORD}@{settings.DATABASEURL}?retryWrites=true&w=majority"
        self.URL=f"mongodb+srv://test1:test1@testbatch.4k43ctn.mongodb.net/?retryWrites=true&w=majority"
        
        self.client=MongoClient(self.URL)
        # self.db=self.client[settings.DATABASENAE]
        self.db=self.client['APIKEY']
        self.collection=self.db['apikey']
        
    def cheak_ping(self):
        return self.client.server_info()
    
    def insert_data(self,data):
        return self.collection.insert_one(data)
    def find_data(self,data):
        return self.collection.find_one(data)
    def find_all_data(self):
        return self.collection.find()
    def delete_data(self,data):
        return self.collection.delete_one(data)
    def count_data(self):
        return self.collection.count_documents({})



