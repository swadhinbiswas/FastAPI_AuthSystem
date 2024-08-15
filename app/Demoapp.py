from fastapi import FastAPI



Apps = FastAPI()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(Apps, host="localhost", port=8000)