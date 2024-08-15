from datetime import datetime,timezone,timedelta
import jwt
from typing import Annotated, Optional
from app.models import TokenData
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from app.settings import settings
from app.models import User
from fastapi import APIRouter


router=APIRouter()
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
oauth2_bearer=OAuth2PasswordBearer(tokenUrl="token")



class JwtFunction:
    def __init__(self) :
      self.algorithm=settings.ALGRITHM
      self.secret_key=settings.SECRETKEY
      self.access_token_expire_minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
      self.refresh_token_expire_minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES
    
   
    def __hashpassword(self,password:str)->str:
        return self.pwd_context.hash(password)
    
    def veryfy_password(self,plain_password:str,hashed_password:str)->bool:
        return self.pwd_context.verify(plain_password,hashed_password)
    def password_encrypt(self,password:str)->str:
        return self.__hashpassword(password)
    
    def authenticate_user(self,database,username:str,password:str):
      user=database.find_data({"username":username})
      if not user:
        return False
      if not self.veryfy_password(password,user["password"]):
        return False
      return user
    
    def create_access_token(self,data:dict,expires_delta:Optional[timedelta]=None):
        to_encode=data.copy()
        if expires_delta:
            expire=datetime.now()+expires_delta
        else:
            expire=datetime.now()+timedelta(minutes=15)
            
        to_encode.update({"exp":expire})
        encoded_jwt=jwt.encode(to_encode,self.secret_key,algorithm=self.algorithm)
        return encoded_jwt
      
    def create_refresh_token(self,data:dict,expires_delta:Optional[timedelta]=None):
        to_encode=data.copy()
        if expires_delta:
            expire=datetime.now()+expires_delta
        else:
            expire=datetime.now()+timedelta(minutes=15)
            
        to_encode.update({"exp":expire})
        encoded_jwt=jwt.encode(to_encode,self.secret_key,algorithm=self.algorithm)
        return encoded_jwt
      
    def decode_token(self,token:str):
        try:
            payload=jwt.decode(token,self.secret_key,algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Token Expired")
        except InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Token")
        except Exception:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Token")
    
    async def get_current_user(self,token:Annotated[str,Depends(oauth2_bearer)])->str:
        credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                            detail="Could not validate credentials",
                                            headers={"WWW-Authenticate":"Bearer"})
        
        try:
            payload=jwt.decode(token,self.secret_key,algorithms=[self.algorithm])
            username:Annotated[str,Optional]=payload.get("sub")
            if username is None:
                raise credentials_exception
            token_data=TokenData(username=username)
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Token Expired")
        except InvalidTokenError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Token")
        except Exception:
            raise credentials_exception
        return username
      
      
    async def get_current_active_user(self,current_user:Annotated[str,Depends(get_current_user)])->User:
        user=User.find_data({"username":current_user})#Need to implement this method Again With Real Database code
        """ Have to update with regular Database And It will contain multiple database """
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
        return user
      


@router.post("/token")
async def login_for_access_token(form_data:OAuth2PasswordRequestForm=Depends()):
    jwt=JwtFunction()
    user=jwt.authenticate_user(form_data.username,form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect username or password")
    access_token_expires=timedelta(minutes=jwt.access_token_expire_minutes)
    refresh_token_expires=timedelta(minutes=jwt.refresh_token_expire_minutes)
    access_token=jwt.create_access_token(data={"sub":user["username"]},expires_delta=access_token_expires)
    refresh_token=jwt.create_refresh_token(data={"sub":user["username"]},expires_delta=refresh_token_expires)
    return {"access_token":access_token,"token_type":settings.TOKEN_TYPE},{"refresh_token":refresh_token}
  
@router.post("/refresh_token")
async def refresh_token(refresh_token:str=Depends()):
    jwt=JwtFunction()
    payload=jwt.decode_token(refresh_token)
    access_token_expires=timedelta(minutes=jwt.access_token_expire_minutes)
    access_token=jwt.create_access_token(data={"sub":payload["sub"]},expires_delta=access_token_expires)
    return {"access_token":access_token,"token_type":settings.TOKEN_TYPE}
  
@router.get("/users/me")
async def read_users_me(current_user:Annotated[str,Depends(get_current_active_user)]):
    return current_user


