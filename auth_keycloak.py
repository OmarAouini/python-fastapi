"""KEYCLOAK AUTHENTICATION MODULE"""
import sys
from typing import Optional
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from jose.constants import ALGORITHMS
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import requests

KEYCLOAK_URL = "http://localhost:8080"

# Why doing this?
# Because we want to fetch public key on start (on import in main module this will run)
# Later we would verify incoming JWT tokens
try:
    r = requests.get(f"{KEYCLOAK_URL}/auth/realms/master",
                     timeout=3)
    r.raise_for_status()
    response_json = r.json()
except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)
    sys.exit(1)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
    sys.exit(1)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
    sys.exit(1)
except requests.exceptions.RequestException as err:
    print("OOps: Something Else", err)
    sys.exit(1)

SECRET_KEY = f'-----BEGIN PUBLIC KEY-----\r\n{response_json["public_key"]}\r\n-----END PUBLIC KEY-----'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class TokenData(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None


class User(BaseModel):
    username: str
    email: str


async def login_jwt(form_data: OAuth2PasswordRequestForm = Depends(), realm: str = "master"):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        r = requests.post(f"{KEYCLOAK_URL}/auth/realms/{realm}/protocol/openid-connect/token", timeout=3)
        r.raise_for_status()
        response_json = r.json()
        return response_json
    except requests.HTTPError as e:
        print(e)
        raise credentials_exception


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHMS.RS256],
                             options={"verify_signature": True, "verify_aud": False, "exp": True})
        username: str = payload.get("preferred_username")
        email =  payload.get('email'),
        token_data = TokenData(username=username, email=email)
    except JWTError as e:
        print(e)
        raise credentials_exception
    return token_data


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    return current_user
