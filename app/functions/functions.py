from typing import NewType
from hashlib import blake2b

import secrets

class HashGen:
  
  """Args:
  key: str
  Returns:
  NewType: str
  Description:
  This function generates a 32 bit hash token using the blake2b algorithm.
  
  
  why blake2b?
  1. It is faster than md5, sha1, sha2, and sha3.
  2. It is more secure than md5, sha1, sha2, and sha3.
  
  and then it returns a token of type NewType.
  
  
  
  
  """
  def __gen32bithash(key:str)->NewType:
    temptoken=secrets.token_urlsafe(16)
    hashlibtoken=blake2b(digest_size=10,key=key.encode())
    token=hashlibtoken.hexdigest()
    finaltoken=temptoken+token
    tokentype=NewType(finaltoken,str)
    return tokentype(finaltoken)
  
  @staticmethod
  def hashgenarator(key:str)->NewType:
    return HashGen.__gen32bithash(key=key)





    
    