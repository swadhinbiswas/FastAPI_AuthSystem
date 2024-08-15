from typing import Optional
from decouple import config
# config.encoding('cp1251')


class Settings:
    DATABASENAE:Optional[str]=config('DATABASENAME')
    DATABASEURL:Optional[str]= config('MONGODBURL')
    DATABASEPASSWORD:Optional[str]=config('MONGODBPASSWORD')
    DATABASEUSER:Optional[str]=config('DATABSEUSER')
    PATHOFAPP:Optional[str]=config('PATHOFAPP')
    ALGRITHM:Optional[str]=config('ALGRITHM')
    SECRETKEY:Optional[str]=config('SECRETKEY')
    ACCESS_TOKEN_EXPIRE_MINUTES:Optional[int]=config('ACCESS_TOKEN_EXPIRE_MINUTES')
    REFRESH_TOKEN_EXPIRE_MINUTES:Optional[int]=config('REFRESH_TOKEN_EXPIRE_MINUTES')
    TOKEN_TYPE:Optional[str]=config('TOKEN_TYPE')
    
    





setting=Settings()


