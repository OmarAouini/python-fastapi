"""MAIN"""
import logging
from fastapi import Depends, FastAPI, HTTPException
import uvicorn

from auth_keycloak import User, get_current_active_user
from database import DB_NAME

# logger
logger = logging.getLogger("uvicorn")

app = FastAPI()
ENV = "dev" #TODO: set dotenv file

# health check endpoint
@app.get("/", status_code=200, tags=["health"])
async def health():
    """healthcheck endpoint"""
    return {"result":"OK"}

# example endpoint with auth user
@app.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

# run
if __name__ == "__main__":
    print("AUTHOR: OMAR AOUINI, 2022")
    print("SAMPLE REST API")
    print(f"ENV: {ENV}")
    print(f"DB NAME: {DB_NAME}")
    print("============================")
    uvicorn.run(app, host="0.0.0.0", port=8080)
