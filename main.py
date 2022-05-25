"""MAIN"""
import logging
from fastapi import FastAPI, Response, HTTPException
import uvicorn

# logger
logger = logging.getLogger("uvicorn")

app = FastAPI()
ENV = "dev" #TODO: set dotenv file
DB_NAME = "employees"

# health check endpoint
@app.get("/", status_code=200)
async def health():
    """healthcheck endpoint"""
    return Response(status_code=200)

# run
if __name__ == "__main__":
    print("AUTHOR: OMAR AOUINI, 2022")
    print("SAMPLE REST API")
    print(f"ENV: {ENV}")
    print(f"DB NAME: {DB_NAME}")
    print("============================")
    uvicorn.run(app, host="0.0.0.0", port=8080)