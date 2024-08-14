# from motor.motor_asyncio import AsyncIOMotorClient
# from contextlib import asynccontextmanager
# from app.settings import setting
# from typing import Dict







#    #Define LifeSpan for MongoDB
    
#     # Close the database connection

#    @asynccontextmanager
#    async def mogolife(app:FastAPI):
#       await startup_db_client(app)
#       yield
#       await shutdown_db_client(app)

#    async def startup_db_client(app):
#         app.mongodb_client = AsyncIOMotorClient(_CONSTRACTEDURL)
#         app.mongodb = app.mongodb_client.get_database("_DATABASENAME")
#         return {
#             database: "Active",
#             function:"Loaded"    
#             }


#    async def shutdown_db_client(app):
#       app.mongodb_client.close()
#    async def save_to_mongodb(key:Dict|str):
#       app.mongodb["_DATABASENAME"].insert_one(key)
#    async def revokekey(key:str):
#       x_key=app.mongodb["_DATABASENAME"].find_one(key)
#       app.mongodb["_DATABASENAME"].delete_one(x_key)

from pymongo import MongoClient
# from app.settings import setting


# class MONGODATABASE:
# #variable for MongoDB
#    # _MONGODBURL=setting.DATABASEURL
#    # _MOGODBUSER=setting.DATABASEUSER
#    # _MOGODBPASS=setting.DATABASEPASSWORD
#    # _DATABASENAME=setting.DATABASENAME
#    # _CONSTRACTEDURL=f"mongodb+srv://{_MOGODBUSER}:{_MOGODBPASS}@{_MONGODBURL}/{_DATABASENAME}"
#    # #mongodb+srv://<username>:<password>@beyondthebasics.abcde.mongodb.net/test
   
#    client=MongoClient("mongodb+srv://test1:test1@testbatch.4k43ctn.mongodb.net/?retryWrites=true&w=majority")
   
#    database=client["APIKEY"]
#    collection=database[""]
    
     
     
   
   
try:
   connection=MongoClient("mongodb+srv://test1:test1@testbatch.4k43ctn.mongodb.net")
   
   print("connected")
   
except Exception as e:
   print(e)
   

