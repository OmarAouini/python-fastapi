"""MAIN"""
import logging
from fastapi import FastAPI, Response, logger
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

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    """test endpoint"""
    logger.warning("warningz")
    return {"item_id": item_id}

# run
if __name__ == "__main__":
    print("AUTHOR: OMAR AOUINI, 2022")
    print("SAMPLE REST API")
    print(f"ENV: {ENV}")
    print(f"DB NAME: {DB_NAME}")
    print("============================")
    uvicorn.run(app, host="0.0.0.0", port=8080)