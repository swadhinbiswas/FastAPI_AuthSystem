from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager
from app.settings.settings import Settings





class MONGODATABASE:
   """
   Function for MongoDD connection
   and Database Save
   Arg: Database url Database name Database Password 

   """
   #Define LifeSpan for MongoDB
   @asynccontextmanager
   async def mogolife(app:FastAPI):
    await startup_db_client(app)
    yield
    # Close the database connection
    await shutdown_db_client(app)
async def startup_db_client(app):
    app.mongodb_client = AsyncIOMotorClient(
        "mongodb+srv://UserName:Password@cluster0.abc.mongodb.net/")
    app.mongodb = app.mongodb_client.get_database("college")
    print("MongoDB connected.")

   