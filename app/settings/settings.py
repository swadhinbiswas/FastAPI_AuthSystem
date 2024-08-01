from typing import Optional
from decouple import config
# config.encoding('cp1251')


class Settings:
    DATABASENAE:Optional[str]=config('DATABASENAME')
    DATABASEURL:Optional[str]= config('MONGODBURL')
    DATABASEURL:Optional[str]=config('DATABASEURL')
    DATABASEUSER:Optional[str]=config('DATABSEUSER')
    PATHOFAPP:Optional[str]=config('PATHOFAPP')





setting=Settings()


