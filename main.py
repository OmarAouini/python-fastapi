from fastapi import FastAPI, Response
import uvicorn


app = FastAPI()
ENV = "dev" #TODO: set dotenv file

# health check endpoint
@app.get("/", status_code=200)
def health():
    """healthcheck endpoint"""
    return Response(status_code=200)

# run
if __name__ == "__main__":
    print("AUTHOR: OMAR AOUINI, 2022")
    print("SAMPLE REST API")
    print(f"ENV: {ENV}")
    print("============================")
    uvicorn.run(app, host="127.0.0.1", port=8000)